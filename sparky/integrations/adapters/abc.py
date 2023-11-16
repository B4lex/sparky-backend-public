import abc
from datetime import datetime, timedelta


class CalendarEntryWrapper(metaclass=abc.ABCMeta):
    entry: object

    @property
    @abc.abstractmethod
    def entry_id(self) -> str:
        ...


class AbstractCalendarAdapter(metaclass=abc.ABCMeta):
    calendar_handle: object

    @abc.abstractmethod
    def create_entry(self, title: str, at: datetime, duration: timedelta) -> CalendarEntryWrapper:
        ...

    @abc.abstractmethod
    def update_entry(
        self, entry_id: str, *, title: str, at: datetime, duration: timedelta, **kwargs
    ) -> CalendarEntryWrapper:
        ...

    @abc.abstractmethod
    def delete_entry(self, entry_id: str) -> None:
        ...

    @abc.abstractmethod
    def get_entry_by_identifier(self, entry_id: str) -> CalendarEntryWrapper:
        ...
