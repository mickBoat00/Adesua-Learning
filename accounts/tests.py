import pytest
from django.contrib.auth import get_user_model

pytestmark = pytest.mark.django_db


def test_create_user_with_username():
    """
    TypeError should be throw when trying to create a user
    without email.
    """
    with pytest.raises(TypeError):
        User = get_user_model()
        user = User.objects.create_user(username="test_user", password="test")
        super_user = User.objects.create_superuser(
            username="test_superuser", password="test"
        )
        assert user.username == "test_user"
        assert super_user.username == "test_superuser"


def test_create_user_method():
    """
    create_user method should create a user with email
    and makes sure the user does not have admin access
    """
    User = get_user_model()
    user = User.objects.create_user(
        email="test@test.com",
        first_name="test_first",
        last_name="test_last",
        password="test",
    )
    assert user.email == "test@test.com"
    assert not user.is_superuser
    assert user.is_staff
    assert user.is_active
    assert not user.first_name == "mick"


def test_create_superuser_method():
    """
    create_superuser method should create a superuser with email
    and admin access
    """
    User = get_user_model()
    user = User.objects.create_superuser(email="test@test.com", password="test")
    assert user.email == "test@test.com"
    assert user.is_superuser
    assert user.is_staff
