import pytest

from sparky.activities.models import Activity
from sparky.activities.services.activity import ActivityService
from sparky.core.exceptions import ProhibitedDeletionError


@pytest.mark.django_db
class TestActivityServiceDelete:
    def test_activity_delete(self, activity):
        assert Activity.objects.count() == 1
        ActivityService.delete(activity)
        assert Activity.objects.count() == 0

    def test_global_activity_delete(self, global_activity):
        assert Activity.objects.count() == 1
        with pytest.raises(ProhibitedDeletionError):
            ActivityService.delete(global_activity)
        assert Activity.objects.count() == 1
