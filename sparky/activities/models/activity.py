from datetime import timedelta

from django.db import models
from django.db.models.functions import Lower
from django.utils.translation import gettext_lazy as _

from sparky.core.models import AbstractTimeStamped


class Activity(AbstractTimeStamped):
    title = models.CharField(_("Title"), max_length=256)
    description = models.TextField(_("Description"), blank=True)
    weight = models.PositiveIntegerField(
        _("Weight"), help_text=_("Weight for activity used for adjusting activity frequency during the randomizing")
    )
    category = models.ForeignKey(
        "activities.ActivityCategory",
        on_delete=models.PROTECT,
        related_name="activities",
        verbose_name=_("Category"),
        null=True,
        blank=True,
    )
    owner = models.ForeignKey("users.User", on_delete=models.PROTECT)
    enabled_for = models.ManyToManyField(
        "users.User",
        through="activities.OngoingActivity",
        related_name="enabled_activities",
        verbose_name=_("Enabled for"),
    )
    duration = models.DurationField(_("Duration"), default=timedelta(hours=1))
    start_time = models.TimeField(_("Start time"))
    end_time = models.TimeField(_("End time"))

    class Meta:
        verbose_name = _("Activity")
        verbose_name_plural = _("Activities")
        indexes = [models.Index(fields=["category"])]
        constraints = [models.UniqueConstraint(Lower("title"), "title", name="unique_title")]

    def __str__(self) -> str:
        return self.title

    @property
    def is_global(self) -> bool:
        return not self.owner
