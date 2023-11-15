from django.db import models
from django.utils.translation import gettext_lazy as _

from sparky.core.models import AbstractTimeStamped


class ActivityCategory(AbstractTimeStamped):
    name = models.CharField(_("Name"), max_length=256)

    class Meta:
        verbose_name = _("Activity category")
        verbose_name_plural = _("Activity categories")

    def __str__(self):
        return self.name
