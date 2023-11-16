from sparky.integrations.adapters import AppleCalendarAdapter, GoogleCalendarAdapter
from sparky.integrations.constants import IntegrationType
from sparky.integrations.models import CalendarEntry


class CalendarEntryService:
    adapter_class_mapping = {
        IntegrationType.GOOGLE_CALENDAR: GoogleCalendarAdapter,
        IntegrationType.APPLE_CALENDAR: AppleCalendarAdapter,
    }

    def __init__(self, calendar_entry: CalendarEntry) -> None:
        self.adapter = self.adapter_class_mapping[IntegrationType(calendar_entry.integration_type)]
