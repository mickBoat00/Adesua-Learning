import factory
from django.contrib.auth import get_user_model
from faker import Faker

from apps.courses.models import Course, Curriculum, Subject

fake = Faker()


print(dir(fake))


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    email = fake.email()
    password = fake.last_name_male()


class CurriculumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Curriculum

    short_name = "GES"
    name = "Ghana Education Service"


class SubjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Subject

    name = fake.word()


class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Course

    title = fake.sentence()
    curriculum = factory.SubFactory(CurriculumFactory)
    subject = factory.SubFactory(SubjectFactory)
    year = 1
    description = fake.sentence()
    price = str(fake.pydecimal(left_digits=3, right_digits=2))
    enrollment_type = fake.random_element(elements=("Free", "Paid"))
    status = fake.random_element(elements=("Approved", "Pending"))
    published_status = fake.pybool()
    instructor = factory.SubFactory(UserFactory)
