import pytest

from sparky.activities.factories.activity import ActivityFactory
from sparky.activities.models import Activity


@pytest.fixture
def activity(db) -> Activity:
    return ActivityFactory()


@pytest.fixture
def global_activity(db) -> Activity:
    return ActivityFactory(owner=None)
