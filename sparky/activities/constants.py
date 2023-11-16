from django.db import models
from django.utils.translation import gettext_lazy as _


class ActivityEventStatus(models.TextChoices):
    PENDING = "PENDING", _("Pending")
    IN_PROGRESS = "IN_PROGRESS", _("In progres")
    REJECTED = "REJECTED", _("Rejected")
    COMPLETED = "COMPLETED", _("Completed")
