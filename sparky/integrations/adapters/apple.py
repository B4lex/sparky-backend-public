from datetime import datetime, timedelta

from sparky.integrations.adapters.abc import AbstractCalendarAdapter, CalendarEntryWrapper


class AppleCalendarAdapter(AbstractCalendarAdapter):
    def create_entry(
        self, title: str, at: datetime, duration: timedelta, description: str | None = None, **kwargs
    ) -> CalendarEntryWrapper:
        ...

    def update_entry(
        self,
        entry_id: str,
        *,
        title: str | None = None,
        at: datetime | None = None,
        duration: timedelta | None = None,
        **kwargs,
    ) -> CalendarEntryWrapper:
        ...

    def delete_entry(self, entry_id: str) -> None:
        ...

    def get_entry_by_identifier(self, entry_id: str) -> CalendarEntryWrapper:
        ...
