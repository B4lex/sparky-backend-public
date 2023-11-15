from django.db import models
from django.utils.translation import gettext_lazy as _

from sparky.core.models import AbstractTimeStamped


class ActivityCompletion(AbstractTimeStamped):
    scheduled_on = models.DateField(_("Scheduled on"))
    completion_time = models.DateTimeField(
        _("Completion time"),
        help_text=_("Describes whether and when activity has been completed for scheduled date"),
        null=True,
        blank=True,
    )
    ongoing_activity = models.ForeignKey(
        "activities.OngoingActivity",
        on_delete=models.CASCADE,
        verbose_name=_("Ongoing activity"),
        related_name="completions",
    )

    class Meta:
        indexes = [models.Index(fields=["scheduled_on"])]

    def __str__(self):
        return f"{self.ongoing_activity} scheduled on: {self.scheduled_on}"

    @property
    def is_completed(self) -> bool:
        return bool(self.completion_time)
