from django.db import models
from django.utils.translation import gettext_lazy as _

from sparky.core.models import AbstractTimeStamped


class OngoingActivity(AbstractTimeStamped):
    """
    Through-model for Activity <-> User M2M relation.
    Represents pool of activities taken by user

    Relates to:
    - FK: User - user that activity is added to their pool
    - FK: Activity - activity template that is added to user
    """

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="ongoing_activities", verbose_name=_("User")
    )
    activity = models.ForeignKey(
        "activities.Activity",
        on_delete=models.PROTECT,
        related_name="ongoing_activities",
        verbose_name=_("Ongoing activity"),
    )
    enabled = models.BooleanField(_("Enabled"), default=True)

    class Meta:
        verbose_name = _("Ongoing activity")
        verbose_name_plural = _("Ongoing activities")

    def __str__(self) -> str:
        return f"Ongoing: {self.activity}"
