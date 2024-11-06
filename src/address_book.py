from collections import UserDict
from datetime import datetime, timedelta

from record import Record

from custom_exceptions import InputException
from custom_exceptions import RecordNotFountException


class AddressBook(UserDict[str, Record]):
    def add_record(self, value: Record):
        if not value:
            raise InputException("Invalid data")

        if self.__is_contact_exists(value.name.value):
            raise InputException("Contact has already exists")

        self.add_key(value.name.value, value)

    def add_key(self, key: str, value: Record):
        self.data[key] = value

    def find(self, key: str) -> Record | None:
        if not self.__is_contact_exists(key):
            raise RecordNotFountException("Couldn't find this contact.")

        return self.data.get(key)

    def remove(self, key: str):
        if not self.__is_contact_exists(key):
            raise RecordNotFountException("Couldn't remove this contact. Record not exists")

        del self.data[key]

    def get_upcoming_birthdays(self):
        pass

    def __is_contact_exists(self, key) -> bool:
        return key in self.data


if __name__ == "__main__":
    addressBook = AddressBook()

    dictActions = [
        { "method": addressBook.add_record, "values": [ Record("Vasya") ] },
        { "method": addressBook.add_record, "values": [ Record("John") ] },
        { "method": addressBook.remove, "values": [ "John" ] },
    ]

    for item in dictActions:
        try:
            values = item["values"]
            item["method"].__call__(*values)

            for name, record in addressBook.data.items():
                print(record)
            print("\n")
        except Exception as e:
            print(f"Values: {values}, error: {e}")

    print(f"found: {addressBook.find("Vasya")}")