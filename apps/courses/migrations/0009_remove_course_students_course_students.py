# Generated by Django 4.2.7 on 2023-12-09 16:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0008_course_students'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(related_name='student_courses', to=settings.AUTH_USER_MODEL),
        ),
    ]