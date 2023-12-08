from rest_framework import permissions, viewsets
from rest_framework.generics import ListAPIView

from .models import Course, Curriculum, Subject
from .permissions import IsOwnerOrReadOnly
from .serializer import (
    CreateCourseSerializer,
    CurriculumSerializer,
    ReadCourseSerializer,
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
    queryset = Course.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    def get_serializer_class(self):
        if self.action in (
            "list",
            "retrieve",
        ):
            return ReadCourseSerializer
        return CreateCourseSerializer

    def perform_create(self, serializer):
        return serializer.save(instructor=self.request.user)
