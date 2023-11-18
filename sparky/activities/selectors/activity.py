from django.db.models import Q, QuerySet

from sparky.activities.models import Activity
from sparky.users.models import User


class ActivitySelectors:
    @staticmethod
    def get_available_activities_for_user(user: User) -> QuerySet[Activity]:
        return Activity.objects.filter(Q(owner__isnull=True) | Q(owner=user))
