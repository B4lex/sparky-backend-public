from sparky.integrations.adapters import AppleCalendarAdapter, GoogleCalendarAdapter
from sparky.integrations.constants import IntegrationType
from sparky.integrations.models import CalendarEntry
from sparky.users.services.user import UserService


class CalendarEntryService:
    adapter_class_mapping = {
        IntegrationType.GOOGLE_CALENDAR: GoogleCalendarAdapter,
        IntegrationType.APPLE_CALENDAR: AppleCalendarAdapter,
    }

    def __init__(self, calendar_entry: CalendarEntry) -> None:
        adapter_class = self.adapter_class_mapping[IntegrationType(calendar_entry.integration_type)]
        self._adapter = adapter_class(
            access_token=UserService.get_google_api_access_token(calendar_entry.user),
            refresh_token=UserService.get_google_api_refresh_token(calendar_entry.user),
        )
