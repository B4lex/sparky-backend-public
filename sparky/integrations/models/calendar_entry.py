from django.db import models
from django.utils.translation import gettext_lazy as _

from sparky.core.models import AbstractTimeStamped
from sparky.integrations.constants import IntegrationType


class CalendarEntry(AbstractTimeStamped):
    """
    Describes entity in the external integration (e.g. Google Calendar)
    """

    integration_type = models.CharField(_("Integration type"), max_length=max(map(len, IntegrationType.values)))
    external_identifier = models.CharField(
        _("External identifier"),
        max_length=256,
        unique=True,
        help_text=_("Unique identifier of the calendar entry in the external system."),
    )
    activity_completion = models.ForeignKey(
        "activities.ActivityEvent",
        on_delete=models.CASCADE,
        related_name="calendar_entries",
        verbose_name=_("Activity completion"),
    )

    def __str__(self) -> str:
        return f"{self.integration_type} entry for {self.activity_completion}"
