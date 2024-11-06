from collections import UserDict
from datetime import datetime, timedelta

from record import Record

from custom_exceptions import InputException
from custom_exceptions import RecordNotFountException


class AddressBook(UserDict[str, Record]):
    def add_record(self, value: Record):
        pass

    def add_key(self, key: str, value: Record):
        pass

    def find(self, key: str) -> Record | None:
        pass

    def remove(self, key: str):
        pass

    def get_upcoming_birthdays(self):
        pass
