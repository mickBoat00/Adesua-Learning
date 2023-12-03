# Generated by Django 4.2.7 on 2023-12-02 15:53

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Curriculum",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now=True)),
                ("updated_on", models.DateTimeField(auto_now_add=True)),
                (
                    "short_name",
                    models.CharField(max_length=10, verbose_name="Code Name"),
                ),
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="Curriculum Name"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]