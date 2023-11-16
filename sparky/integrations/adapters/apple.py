from datetime import datetime, timedelta

from sparky.integrations.adapters.abc import AbstractCalendarAdapter, CalendarEntryWrapper


class AppleCalendarAdapter(AbstractCalendarAdapter):
    def create_entry(
        self, title: str, at: datetime, duration: timedelta, *, notify_user_before: timedelta | None = None
    ) -> CalendarEntryWrapper:
        ...

    def update_entry(
        self, entry_id: str, *, title: str, at: datetime, duration: timedelta, **kwargs
    ) -> CalendarEntryWrapper:
        ...

    def delete_entry(self, entry_id: str) -> None:
        ...

    def get_entry_by_identifier(self, entry_id: str) -> CalendarEntryWrapper:
        ...
