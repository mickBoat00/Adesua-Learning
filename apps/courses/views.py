from django.db.models import Q
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Course, Curriculum, Lesson, Subject
from .paystack import Paystack
from .serializers import (
    CreateCourseSerializer,
    CreateLessonSerializer,
    CurriculumSerializer,
    DetailCourseSerializer,
    ListCourseSerializer,
    PayForCourseSerializer,
    ReadLessonSerializer,
    SubjectSerializer,
)


class CurriculumListView(generics.ListAPIView):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer


class SubjectModelViewset(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class CourseModelViewset(viewsets.ModelViewSet):
    queryset = Course.objects.prefetch_related("lessons", "students").select_related(
        "curriculum", "subject", "instructor"
    )

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly,
    )
    # filter_backends = [filters.SearchFilter]
    # search_fields = ["title", "subject__name"]
    filterset_fields = [
        "curriculum__short_name",
    ]

    def get_serializer_class(self):
        if self.action == "list":
            return ListCourseSerializer

        if self.action == "retrieve":
            return (
                DetailCourseSerializer
                if self.request.user in self.get_object().students.all()
                else ListCourseSerializer
            )

        if self.action == "enroll":
            return PayForCourseSerializer
        return CreateCourseSerializer

    def perform_create(self, serializer):
        return serializer.save(instructor=self.request.user)

    @action(detail=True, methods=["post", "delete"])
    def enroll(self, request, pk=None):
        if request.method == "POST":
            course = self.get_object()

            user = request.user

            user_courses = list(
                Course.objects.filter(
                    Q(instructor=user) | Q(students=user)
                ).values_list("id", flat=True)
            )

            if course.id in user_courses:
                return Response(
                    {
                        "error": "Cannot enroll user in these course because he is an instructor or a student"
                    },
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                )

            serializer = PayForCourseSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            paystack = Paystack()
            response = paystack.charge(
                course.price, user.email, serializer.data["mobile_number"]
            )

            return Response(response.json()["data"], status=response.status_code)


class LessonModelViewset(viewsets.ModelViewSet):
    queryset = Lesson.objects.select_related("course")

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadLessonSerializer
        return CreateLessonSerializer
