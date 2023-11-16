from sparky.activities.models import ActivityEvent
from sparky.integrations.adapters import AppleCalendarAdapter, GoogleCalendarAdapter
from sparky.integrations.adapters.abc import AbstractCalendarAdapter
from sparky.integrations.constants import IntegrationType
from sparky.integrations.models import CalendarEntry
from sparky.users.models import User
from sparky.users.services.user import UserService


class CalendarEntryService:
    adapter_class_mapping = {
        IntegrationType.GOOGLE_CALENDAR: GoogleCalendarAdapter,
        IntegrationType.APPLE_CALENDAR: AppleCalendarAdapter,
    }

    @classmethod
    def _get_adapter(cls, integration_type: IntegrationType, user: User) -> AbstractCalendarAdapter:
        adapter_class = cls.adapter_class_mapping[IntegrationType(integration_type)]
        return adapter_class(
            access_token=UserService.get_google_api_access_token(user),
            refresh_token=UserService.get_google_api_refresh_token(user),
        )

    @classmethod
    def create(
        cls, event: ActivityEvent, integration_type: IntegrationType = IntegrationType.GOOGLE_CALENDAR
    ) -> CalendarEntry:
        adapter = cls._get_adapter(integration_type, event.user)
        entry_wrapper = adapter.create_entry(
            title=event.template.title,
            description=event.template.description,
            at=event.scheduled_on,
            duration=event.template.duration,
        )
        return CalendarEntry.objects.create(
            integration_type=integration_type, activity_event=event, external_identifier=entry_wrapper.entry_id
        )
