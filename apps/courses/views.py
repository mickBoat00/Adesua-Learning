from rest_framework import permissions, viewsets
from rest_framework.generics import ListAPIView

from .models import Course, Curriculum, Lesson, Subject
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    CreateCourseSerializer,
    CreateLessonSerializer,
    CurriculumSerializer,
    DetailCourseSerializer,
    ListCourseSerializer,
    ReadLessonSerializer,
    SubjectSerializer,
)


class CurriculumListView(ListAPIView):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer


class SubjectModelViewset(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class CourseModelViewset(viewsets.ModelViewSet):
    queryset = Course.objects.prefetch_related("lessons").select_related(
        "curriculum", "subject", "instructor"
    )
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    def get_serializer_class(self):
        if self.action == "list":
            return ListCourseSerializer

        if self.action == "retrieve":
            return DetailCourseSerializer
        return CreateCourseSerializer

    def perform_create(self, serializer):
        return serializer.save(instructor=self.request.user)


class LessonModelViewset(viewsets.ModelViewSet):
    queryset = Lesson.objects.select_related("course")

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadLessonSerializer
        if self.action == "create":
            return CreateLessonSerializer
