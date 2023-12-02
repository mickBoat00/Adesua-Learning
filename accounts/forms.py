from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    """
    Override the default UserCreationForm with new custom user.
    """

    class Meta:
        model = User
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    """
    Override the default UserChangeForm with new custom user.
    """

    class Meta:
        model = User
        fields = ("email",)
