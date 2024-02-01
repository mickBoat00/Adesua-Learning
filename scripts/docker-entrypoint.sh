#!/bin/bash

python manage.py makemigrations
python manage.py migrate

python manage.py collectstatic

gunicorn --bind :8000 --workers 4 adesua.wsgi:application

exec "$@"
