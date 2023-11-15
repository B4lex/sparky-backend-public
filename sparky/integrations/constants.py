from django.db import models
from django.utils.translation import gettext_lazy as _


class IntegrationType(str, models.TextChoices):
    GOOGLE_CALENDAR = "GOOGLE_CALENDAR", _("Google Calendar")
    APPLE_CALENDAR = "APPLE_CALENDAR", _("Apple Calendar")
