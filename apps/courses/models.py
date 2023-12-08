from decimal import Decimal

from autoslug import AutoSlugField
from django.conf import settings
from django.core.validators import FileExtensionValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class TimeStampModel(models.Model):
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Curriculum(TimeStampModel):
    short_name = models.CharField(_("Code Name"), max_length=10)
    name = models.CharField(_("Curriculum Name"), max_length=100)

    class Meta:
        verbose_name_plural = _("Curricula")

    def __str__(self):
        return self.name


class Subject(TimeStampModel):
    name = models.CharField(_("Subject Name"), max_length=100)

    def __str__(self):
        return self.name


class Course(TimeStampModel):
    YEAR = [(i, i) for i in range(1, 13)]

    PAY_CHOICES = [
        ("Free", "Free"),
        ("Paid", "Paid"),
    ]

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
    ]

    title = models.CharField(verbose_name=_("Course Title"), max_length=100)
    slug = AutoSlugField(
        populate_from="title", editable=False, unique=True, always_update=True
    )
    curriculum = models.ForeignKey(
        Curriculum, on_delete=models.CASCADE, verbose_name=_("Course Syllables")
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.PROTECT, verbose_name=_("Course Subject")
    )
    year = models.CharField(
        verbose_name=_("Year"),
        max_length=2,
        choices=YEAR,
    )
    description = models.TextField()
    cover_image = models.ImageField(
        verbose_name=_("Main Image"), upload_to="course_images", null=True, blank=True
    )
    price = models.DecimalField(
        verbose_name=_("Price"),
        max_digits=8,
        decimal_places=2,
        default=0.0,
        validators=[MinValueValidator(Decimal("0.00"))],
    )

    enrollment_type = models.CharField(
        verbose_name=_("Paid / Free"),
        max_length=4,
        choices=PAY_CHOICES,
        default="Free",
    )

    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Course Instructor"),
        related_name="courses",
        on_delete=models.CASCADE,
    )

    status = models.CharField(
        verbose_name=_("Status"),
        max_length=8,
        choices=STATUS_CHOICES,
        default="Pending",
    )

    published_status = models.BooleanField(
        verbose_name=_("Published Status"), default=False
    )

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def save(self, *args, **kwargs):
        self.title = str.title(self.title)
        if self.enrollment_type == "Free":
            self.price = 0.00
        if self.status == "Approved":
            self.published_status = True
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Lesson(TimeStampModel):
    course = models.ForeignKey(
        Course,
        verbose_name=_("Course Lesson"),
        on_delete=models.CASCADE,
        related_name="lessons",
    )
    title = models.CharField(verbose_name=_("Lesson Title"), max_length=255)
    video = models.FileField(
        verbose_name=_("Lesson Title"),
        upload_to="course_lessons",
        validators=[FileExtensionValidator(["mp4", "webm", "mkv", "flv"])],
    )

    def __str__(self):
        return self.title
