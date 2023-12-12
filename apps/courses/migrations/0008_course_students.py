# Generated by Django 4.2.7 on 2023-12-09 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0007_alter_lesson_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='student_courses', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]