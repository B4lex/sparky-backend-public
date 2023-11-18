import typing

from sparky.activities.models import OngoingActivity

if typing.TYPE_CHECKING:
    from django.db.models import QuerySet

    from sparky.users.models import User


class OngoingActivitySelectors:
    @staticmethod
    def get_ongoing_activities_for_user(user: "User") -> "QuerySet[OngoingActivity]":
        return user.ongoing_activities.all()
