import pytest
from django.utils import timezone

from sparky.activities.constants import ActivityEventStatus
from sparky.activities.models import ActivityEvent
from sparky.activities.services import ActivityEventService
from sparky.integrations.services import CalendarEntryService


class TestActivityEventServiceCreate:
    @pytest.fixture
    def mocked_calendar_entry_create(self, mocker):
        return mocker.patch.object(CalendarEntryService, "create")

    def test_event_created_along_with_calendar_entry(self, ongoing_activity, mocked_calendar_entry_create):
        expected_scheduled_on = timezone.now()
        assert ActivityEvent.objects.count() == 0
        event = ActivityEventService.create(ongoing_activity, expected_scheduled_on)
        assert ActivityEvent.objects.count() == 1
        assert event.scheduled_on == expected_scheduled_on
        assert event.ongoing_activity_id == ongoing_activity.id
        mocked_calendar_entry_create.assert_called_once_with(event)


class TestActivityServiceStatus:
    @pytest.mark.freeze_time()
    def test_complete_order(self, activity_event):
        expected_completion_time = timezone.now()
        ActivityEventService.complete_event(activity_event)
        assert activity_event.completion_time == expected_completion_time
        assert activity_event.status == ActivityEventStatus.COMPLETED
