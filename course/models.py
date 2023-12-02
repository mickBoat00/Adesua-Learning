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

    def __str__(self):
        return self.name


# class Course(TimeStampModel):

#     # CURRICULUM = [
#     #     ("American", "American"),
#     #     ("A-Level", "A-Level"),
#     #     ("IGCSE", "IGCSE"),
#     #     ("IB", "International Baccalaureate"),
#     #     ("CIE", "Cambridge International Examinations"),
#     #     ("GCSE", "General Certificate of Secondary Education"),
#     #     ("GES", "Ghana Education System"),
#     # ]


#     YEAR = [ (i, i ) for i in range(1,13)]

#     PAY_CHOICES = [
#         ("Free", "Free"),
#         ("Paid", "Paid"),
#     ]

#     STATUS_CHOICES = [
#         ("Pending", "Pending"),
#         ("Approved", "Approved"),
#     ]

#     year = models.CharField(
#         verbose_name=_("Year"),
#         max_length=2,
#         choices=YEAR,
#     )
#     curriculum = models.ForeignKey(Curriculum, verbose_name=_("Course Syllables"), on_delete=models.CASCADE)
#     instructor = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         verbose_name=_("Course Instructor"),
#         related_name="courses",
#         on_delete=models.CASCADE,
#     )
#     title = models.CharField(verbose_name=_("Course Title"), max_length=100)
#     slug = AutoSlugField(verbose_name=_("Slug"), populate_from="title", editable=False, unique=True, always_update=True)
#     subject = models.CharField(verbose_name=_("Course Subject"), max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(
#         verbose_name=_("Price"),
#         max_digits=8,
#         decimal_places=2,
#         default=0.0,
#         validators=[MinValueValidator(Decimal("0.00"))],
#     )

#     enrollment_type = models.CharField(
#         verbose_name=_("Paid / Free"),
#         max_length=4,
#         choices=PAY_CHOICES,
#         default="Free",
#     )

#     status = models.CharField(
#         verbose_name=_("Status"),
#         max_length=8,
#         choices=STATUS_CHOICES,
#         default="Pending",
#     )

#     published_status = models.BooleanField(verbose_name=_("Published"), default=False)

#     class Meta:
#         verbose_name = _("Course")
#         verbose_name_plural = _("Courses")
#         ordering = ("-created_on",)

#     def save(self, *args, **kwargs):
#         self.title = str.title(self.title)
#         if self.enrollment_type == "Free":
#             self.price = 0.00
#         super(Course, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.title
