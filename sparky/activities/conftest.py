import pytest

from sparky.activities.factories.activity import ActivityFactory
from sparky.activities.factories.event import ActivityEventFactory
from sparky.activities.factories.ongoing_activity import OngoingActivityFactory
from sparky.activities.models import Activity, ActivityEvent, OngoingActivity


@pytest.fixture
def activity(db) -> Activity:
    return ActivityFactory()


@pytest.fixture
def global_activity(db) -> Activity:
    return ActivityFactory(owner=None)


@pytest.fixture
def ongoing_activity(db) -> OngoingActivity:
    return OngoingActivityFactory()


@pytest.fixture
def activity_event(db) -> ActivityEvent:
    return ActivityEventFactory()
