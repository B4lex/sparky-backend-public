import abc
from datetime import time, timedelta


class CalendarEntryWrapper(metaclass=abc.ABCMeta):
    entry: object

    @property
    @abc.abstractmethod
    def entry_id(self) -> str:
        ...


class AbstractCalendarAdapter(metaclass=abc.ABCMeta):
    calendar_handle: object

    @classmethod
    @abc.abstractmethod
    def create_entry(
        cls, title: str, start_time: time, duration: timedelta, *, notify_user_before: timedelta | None = None
    ) -> CalendarEntryWrapper:
        ...

    @classmethod
    @abc.abstractmethod
    def update_entry(cls) -> CalendarEntryWrapper:
        ...

    @classmethod
    @abc.abstractmethod
    def delete_entry(cls, entry_id: str) -> None:
        ...

    @classmethod
    @abc.abstractmethod
    def get_entry_by_identifier(cls, entry_id: str) -> CalendarEntryWrapper:
        ...
