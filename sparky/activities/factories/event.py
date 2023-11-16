import factory.fuzzy
from django.utils import timezone

from sparky.activities.factories.ongoing_activity import OngoingActivityFactory
from sparky.activities.models import ActivityEvent


class ActivityEventFactory(factory.django.DjangoModelFactory):
    scheduled_on = factory.fuzzy.FuzzyDateTime(timezone.now())
    ongoing_activity = factory.SubFactory(OngoingActivityFactory)

    class Meta:
        model = ActivityEvent
