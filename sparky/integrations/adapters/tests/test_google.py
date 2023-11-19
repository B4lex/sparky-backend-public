from datetime import datetime, timedelta

import pytest
from gcsa.event import Event

from sparky.integrations.adapters import GoogleCalendarAdapter


class TestGoogleCalendarAdapter:
    @pytest.fixture
    def access_token(self):
        return "test-access-token"

    @pytest.fixture
    def adapter(self, access_token):
        return GoogleCalendarAdapter(access_token=access_token)

    @pytest.fixture
    def event(self, mocker):
        return mocker.Mock(name="Google Calendar event mock")

    @pytest.fixture
    def mocked_get_event(self, mocker, event):
        return mocker.patch("gcsa.google_calendar.GoogleCalendar.get_event", return_value=event)

    @pytest.fixture
    def mocked_add_event(self, mocker, event):
        return mocker.patch("gcsa.google_calendar.GoogleCalendar.add_event", return_value=event)

    @pytest.fixture
    def mocked_update_event(self, mocker, event):
        return mocker.patch("gcsa.google_calendar.GoogleCalendar.update_event", return_value=event)

    @pytest.fixture
    def mocked_delete_event(self, mocker):
        return mocker.patch("gcsa.google_calendar.GoogleCalendar.get_event", return_value=None)

    def test_create_entry(self, adapter, event, mocked_add_event):
        title = "Test event title"
        at = datetime.now()
        duration = timedelta(minutes=30)
        description = "Test event description"
        wrapper = adapter.create_entry(title, at, duration, description)

        assert wrapper.entry == event
        mocked_add_event.assert_called_once_with(
            Event(summary=title, start=at, end=at + duration, description=description)
        )

    def test_update_entry(self, adapter, event, mocked_update_event, mocked_get_event):
        at = datetime.now()
        description = "Test event description"
        event_id = "test-event-id"
        wrapper = adapter.update_entry(event_id, at=at, description=description)

        assert wrapper.entry.description == description
        assert wrapper.entry.start == at
        mocked_update_event.assert_called_once_with(event)
