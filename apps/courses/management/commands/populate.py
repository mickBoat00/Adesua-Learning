import random
from decimal import Decimal
from typing import Any

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandParser

from apps.courses.models import Course, Curriculum, Subject


class Command(BaseCommand):
    help = "Populate the db with some courses"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "total-courses", type=int, help="Indicate the number of users to create."
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        if get_user_model().objects.count() < 1:
            self.stdout.write(
                self.style.WARNING("Add some users before running this command.")
            )
            return

        total_courses = options["total-courses"]

        curricula = [
            Curriculum(short_name="American", name="American"),
            Curriculum(short_name="A-Level", name="A-Level"),
            Curriculum(
                short_name="IGCSE",
                name="International General Certificate of Secondary Education",
            ),
            Curriculum(short_name="IB", name="International Baccalaureate"),
            Curriculum(short_name="CIE", name="Cambridge International Examinations"),
            Curriculum(
                short_name="GSCE", name="General Certificate of Secondary Education"
            ),
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

        for i in range(total_courses):
            random_subject = random.choice(list(Subject.objects.all()))
            year = random.choice([i for i in range(1, 13)])
            random_instructor = random.choice(get_user_model().objects.all())
            enrollment_type = random.choice(["Paid", "Free"])

            c = Course(
                title=f"{random_subject.name} for {i}year {year}",
                curriculum=random.choice(list(Curriculum.objects.all())),
                subject=random_subject,
                year=year,
                description=f"A course for year {year} on {random_subject.name} by {random_instructor.email}",
                price=Decimal(random.randrange(10, 500))
                if enrollment_type == "Paid"
                else Decimal(0.00),
                enrollment_type=enrollment_type,
                instructor=random_instructor,
                status="Approved",
                published_status=True,
            )
            courses.append(c)

        Course.objects.bulk_create(courses)

        self.stdout.write(self.style.SUCCESS(f"Created {total_courses} courses."))
        return
