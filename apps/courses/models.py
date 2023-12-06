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
