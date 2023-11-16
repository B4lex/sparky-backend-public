from datetime import time, timedelta

from sparky.integrations.adapters.abc import AbstractCalendarAdapter, CalendarEntryWrapper


class GoogleCalendarAdapter(AbstractCalendarAdapter):
    @classmethod
    def create_entry(
        cls, title: str, start_time: time, duration: timedelta, *, notify_user_before: timedelta | None = None
    ) -> CalendarEntryWrapper:
        ...

    @classmethod
    def update_entry(cls) -> CalendarEntryWrapper:
        ...

    @classmethod
    def delete_entry(cls, entry_id: str) -> None:
        ...

    @classmethod
    def get_entry_by_identifier(cls, entry_id: str) -> CalendarEntryWrapper:
        ...
