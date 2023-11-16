import factory.fuzzy

from sparky.activities.factories.activity import ActivityFactory
from sparky.activities.models import OngoingActivity
from sparky.users.tests.factories import UserFactory


class OngoingActivityFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    activity = factory.SubFactory(ActivityFactory)

    class Meta:
        model = OngoingActivity
        django_get_or_create = ("user", "activity")
