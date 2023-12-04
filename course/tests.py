import pytest
from django.urls import reverse
from rest_framework.test import APIClient

client = APIClient()

pytestmark = pytest.mark.django_db


def test_curriculum_endpoint():
    url = reverse("curriculum")
    response = client.get(url)
    assert response.status_code == 200
