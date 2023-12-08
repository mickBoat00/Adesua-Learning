import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.courses.models import Course, Curriculum
from apps.courses.serializers import CurriculumSerializer, ReadCourseSerializer

client = APIClient()


pytestmark = pytest.mark.django_db


def test_curriculum_endpoint_get_method(curriculum):
    url = reverse("curriculum")
    response = client.get(url)
    curricula = Curriculum.objects.all()
    serializer = CurriculumSerializer(curricula, many=True)
    assert response.status_code == status.HTTP_200_OK
    assert serializer.data == response.json()


def test_curriculum_post_method_not_acceptable():
    url = reverse("curriculum")
    response = client.post(url, {"short_name": "NC", "name": "New cur"})
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


def test_course_endpoint_get_method(course):
    response = client.get("/api/courses/")
    courses = Course.objects.all()
    serializer = ReadCourseSerializer(courses, many=True)
    assert response.status_code == status.HTTP_200_OK
    assert serializer.data == response.json()
