from django.utils.translation import gettext_lazy as _

from sparky.activities.models import Activity
from sparky.core.exceptions import ProhibitedDeletionError


class ActivityService:
    @staticmethod
    def delete(activity: Activity) -> None:
        if activity.is_global:
            raise ProhibitedDeletionError(_("Global activities cannot be deleted"))
        activity.delete()
