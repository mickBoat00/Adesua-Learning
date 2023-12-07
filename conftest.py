from pytest_factoryboy import register

from apps.courses.factory import (
    CourseFactory,
    CurriculumFactory,
    SubjectFactory,
    UserFactory,
)

register(UserFactory)
register(CurriculumFactory)
register(SubjectFactory)
register(CourseFactory)
