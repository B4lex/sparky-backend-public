import dataclasses
from datetime import datetime, timedelta

from django.conf import settings
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from google.oauth2.credentials import Credentials

from sparky.integrations.adapters.abc import AbstractCalendarAdapter, CalendarEntryWrapper


@dataclasses.dataclass
class GoogleCalendarEntryWrapper(CalendarEntryWrapper):
    entry: Event

    @property
    def entry_id(self) -> str:
        return self.entry.id


class GoogleCalendarAdapter(AbstractCalendarAdapter):
    calendar_handle: GoogleCalendar

    def __init__(self, *, access_token: str | None, refresh_token: str | None = None):
        credentials = Credentials(
            token=access_token, refresh_token=refresh_token, scopes=[settings.GOOGLE_OAUTH_CALENDAR_SCOPE]
        )
        self.calendar_handle = GoogleCalendar(credentials=credentials)

    def create_entry(
        self, title: str, at: datetime, duration: timedelta, description: str | None = None, **kwargs
    ) -> GoogleCalendarEntryWrapper:
        if not description:
            description = "Automatically created by Sparky."
        event = Event(summary=title, start=at, end=at + duration, description=description, **kwargs)
        entry = self.calendar_handle.add_event(event)
        return GoogleCalendarEntryWrapper(entry)

    def update_entry(
        self,
        entry_id: str,
        *,
        title: str | None = None,
        at: datetime | None = None,
        duration: timedelta | None = None,
        description: str | None = None,
        **kwargs,
    ) -> GoogleCalendarEntryWrapper:
        entry_wrapper = self.get_entry_by_identifier(entry_id)
        event = entry_wrapper.entry
        if title:
            event.summary = title
        if at:
            event.start = at
        if duration:
            event.end = event.start + duration

        # Updating extra properties
        for k, v in kwargs.items():
            setattr(event, k, v)

        event = self.calendar_handle.update_event(event)
        return GoogleCalendarEntryWrapper(event)

    def delete_entry(self, entry_id: str) -> None:
        self.calendar_handle.delete_event(entry_id)

    def get_entry_by_identifier(self, entry_id: str) -> GoogleCalendarEntryWrapper:
        return GoogleCalendarEntryWrapper(self.calendar_handle.get_event(entry_id))
