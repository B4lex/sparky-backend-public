from datetime import datetime

from django.utils import timezone

from sparky.activities.constants import ActivityEventStatus
from sparky.activities.models import ActivityEvent, OngoingActivity
from sparky.integrations.services import CalendarEntryService


class ActivityEventService:
    @staticmethod
    def create(ongoing_activity: OngoingActivity, scheduled_on: datetime) -> ActivityEvent:
        event = ActivityEvent.objects.create(
            ongoing_activity=ongoing_activity,
            scheduled_on=scheduled_on,
        )
        CalendarEntryService.create(event)
        return event

    @staticmethod
    def complete_event(event: ActivityEvent) -> None:
        event.status = ActivityEventStatus.COMPLETED
        event.completion_time = timezone.now()
        event.save()
