# Generated by Django 4.2.7 on 2023-12-06 11:14

import autoslug.fields
from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0002_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Course Title')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title', unique=True)),
                ('year', models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], max_length=2, verbose_name='Year')),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Price')),
                ('enrollment_type', models.CharField(choices=[('Free', 'Free'), ('Paid', 'Paid')], default='Free', max_length=4, verbose_name='Paid / Free')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=8, verbose_name='Status')),
                ('published_status', models.BooleanField(default=False, verbose_name='Published Status')),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.curriculum', verbose_name='Course Syllables')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to=settings.AUTH_USER_MODEL, verbose_name='Course Instructor')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.subject', verbose_name='Course Subject')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
    ]
