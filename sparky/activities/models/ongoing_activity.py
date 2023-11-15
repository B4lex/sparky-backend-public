from django.db import models
from django.utils.translation import gettext_lazy as _

from sparky.core.models import AbstractTimeStamped


class OngoingActivity(AbstractTimeStamped):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="ongoing_activities", verbose_name=_("User")
    )
    activity = models.ForeignKey(
        "activities.Activity",
        on_delete=models.PROTECT,
        related_name="ongoing_activities",
        verbose_name=("Ongoing activity"),
    )

    class Meta:
        verbose_name = _("Ongoing activity")
        verbose_name_plural = _("Ongoing activities")
