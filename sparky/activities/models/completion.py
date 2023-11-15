from django.db import models
from django.utils.translation import gettext_lazy as _

from sparky.core.models import AbstractTimeStamped


class ActivityCompletion(AbstractTimeStamped):
    scheduled_on = models.DateField(_("Scheduled on"))
    completion_time = models.DateTimeField(_("Completion time"), null=True, blank=True)
    ongoing_activity = models.ForeignKey(
        "activities.OngoingActivity",
        on_delete=models.CASCADE,
        verbose_name=_("Ongoing activity"),
        related_name="completions",
    )

    class Meta:
        indexes = [models.Index(fields=["scheduled_on"])]

    @property
    def is_completed(self) -> bool:
        return bool(self.completion_time)
