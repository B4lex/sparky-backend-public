from django.db import models
from django.utils.translation import gettext_lazy as _

from sparky.activities.constants import ActivityEventStatus
from sparky.activities.models import Activity
from sparky.core.models import AbstractTimeStamped
from sparky.users.models import User


class ActivityEvent(AbstractTimeStamped):
    scheduled_on = models.DateTimeField(_("Scheduled on"))
    status = models.CharField(
        _("Status"),
        max_length=max(map(len, ActivityEventStatus.values)),
        choices=ActivityEventStatus.choices,
        default=ActivityEventStatus.PENDING,
    )
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
        related_name="events",
    )

    class Meta:
        indexes = [models.Index(fields=["scheduled_on"]), models.Index(fields=["status"])]

    def __str__(self):
        return f"{self.ongoing_activity} scheduled on: {self.scheduled_on}"

    @property
    def is_completed(self) -> bool:
        return bool(self.completion_time)

    @property
    def user(self) -> User:
        return self.ongoing_activity.user

    @property
    def template(self) -> Activity:
        return self.ongoing_activity.activity
