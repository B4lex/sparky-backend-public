from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class AbstractTimeStamped(models.Model):
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    created_at = models.DateTimeField(_("Created at"), default=timezone.now)

    class Meta:
        abstract = True

    def __str__(self):
        return f"<{self.__class__.__name__} PK: {self.pk}> - created at {self.created_at}"

    def __repr__(self):
        return str(self)
