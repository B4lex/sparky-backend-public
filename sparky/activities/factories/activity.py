import random
from datetime import datetime, time, timedelta

import factory.fuzzy

from sparky.activities.models import Activity
from sparky.users.tests.factories import UserFactory


class ActivityFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("sentence", nb_words=2)
    description = factory.Faker("sentence")
    weight = factory.fuzzy.FuzzyInteger(10, 1000)
    owner = factory.SubFactory(UserFactory)
    start_time = factory.LazyFunction(lambda: time(random.randint(8, 15)))
    end_time = factory.LazyAttribute(
        lambda activity: ((datetime.combine(datetime.now(), activity.start_time) + timedelta(hours=6)).time())
    )

    class Meta:
        model = Activity
        django_get_or_create = ("title",)
