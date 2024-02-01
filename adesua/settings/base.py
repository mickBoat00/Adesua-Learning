"""
Django settings for adesua project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third party apps
    "rest_framework",
    "djoser",
    "drf_spectacular",
    "django_filters",
    # local apps
    "apps.courses",
    "apps.accounts",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

ROOT_URLCONF = "adesua.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "adesua.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


AUTH_USER_MODEL = "accounts.User"


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 10,
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(minutes=360),
}


SPECTACULAR_SETTINGS = {
    "TITLE": "Adesua Learning Backend",
    "DESCRIPTION": "Backend of Adesua Application",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SCHEMA_PATH_PREFIX": "/api/",
    "COMPONENT_SPLIT_REQUEST": True,
}

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR.parent / "static"
STATICFILES_DIR = []
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR.parent / "media"


DJOSER = {
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": False,
    "SEND_ACTIVATION_EMAIL": False,
    "SEND_CONFIRMATION_EMAIL": False,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": False,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": False,
    "SET_PASSWORD_RETYPE": False,
    "PASSWORD_RESET_CONFIRM_RETYPE": False,
    # "USERNAME_RESET_CONFIRM_URL": "email/reset/confirm/{uid}/{token}",
    # "ACTIVATION_URL": "activate/{uid}/{token}",
    # "SERIALIZERS": {
    #     "user_create": "apps.users.serializers.CreateUserSerializer",
    #     "user": "apps.users.serializers.UserSerializer",
    #     "current_user": "apps.users.serializers.UserSerializer",
    #     "user_delete": "djoser.serializers.UserDeleteSerializer",
    # },
}

PAYSTACK_SECRET_KEY = os.environ["PAYSTACK_SECRET_KEY"]
