# ruff: noqa: F405
# ruff: noqa: F403

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ["DEBUG"]


ALLOWED_HOSTS = os.environ["ALLOWED_HOSTS"].split(",")

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": os.environ["POST_HOST"],
        "PORT": os.environ["PG_PORT"],
    }
}
