import random
from decimal import Decimal

from django.contrib.auth import get_user_model

from apps.courses.models import Course, Curriculum, Subject

curricula = [
    Curriculum(short_name="American", name="American"),
    Curriculum(short_name="A-Level", name="A-Level"),
    Curriculum(
        short_name="IGCSE",
        name="International General Certificate of Secondary Education",
    ),
    Curriculum(short_name="IB", name="International Baccalaureate"),
    Curriculum(short_name="CIE", name="Cambridge International Examinations"),
    Curriculum(short_name="GSCE", name="General Certificate of Secondary Education"),
    Curriculum(short_name="GES", name="Ghana Education System"),
]
Curriculum.objects.bulk_create(curricula)


subjects = [
    Subject(name="English"),
    Subject(name="French"),
    Subject(name="Literature"),
    Subject(name="Geography"),
    Subject(name="History"),
    Subject(name="Mathematics"),
    Subject(name="Biology"),
    Subject(name="Chemistry"),
    Subject(name="Physical Education"),
    Subject(name="Physics"),
    Subject(name="ICT"),
    Subject(name="Art"),
]
Subject.objects.bulk_create(subjects)

courses = []
for i in range(1000):
    random_subject = random.choice(list(Subject.objects.all()))
    year = random.choice([i for i in range(1, 13)])
    random_instructor = random.choice(get_user_model().objects.all())
    c = Course(
        title=f"{random_subject.name} for {year} {i}",
        curriculum=random.choice(list(Curriculum.objects.all())),
        subject=random_subject,
        year=year,
        description=f"A course for year {year} on {random_subject.name} by {random_instructor.email}",
        price=Decimal(random.randrange(10, 500)),
        enrollment_type=random.choice(["Paid", "Free"]),
        instructor=random_instructor,
        status="Approved",
        published_status=True,
    )
    courses.append(c)


Course.objects.bulk_create(courses)
