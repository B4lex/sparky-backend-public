from sparky.activities.models import Activity


class ActivitySelectors:
    @staticmethod
    def get_existing_activities():
        return Activity.objects.all()
