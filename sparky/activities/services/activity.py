from sparky.activities.models import Activity


class ActivityService:
    @staticmethod
    def delete(activity: Activity) -> None:
        if not activity.is_global:
            activity.delete()
