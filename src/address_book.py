import pickle

from collections import UserDict
from pathlib import Path
from datetime import datetime, timedelta

from .record import Record

from .custom_exceptions import InputException
from .custom_exceptions import RecordNotFountException


class AddressBook(UserDict[str, Record]):
    def __init__(self, filename: str = "./data/addressbook.dat"):
        super().__init__()
        self.filepath = Path(filename)

    def add_record(self, record: Record):
        if not record:
            raise InputException("Invalid data")

        if self.__is_contact_exists(record.name.value):
            raise InputException("Contact has already exists")

        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        if not self.__is_contact_exists(name):
            raise RecordNotFountException("Couldn't find this contact.")

        return self.data[name]

    def remove(self, name: str):
        if not self.__is_contact_exists(name):
            raise RecordNotFountException(
                "Couldn't remove this contact. Record not exists"
            )

        del self.data[name]

    def get_upcoming_birthdays(self):
        pass

    def save_data(self):
        with self.filepath.open("wb") as file:
            pickle.dump(self, file)

    def load_data(self):
        try:
            with self.filepath.open("rb") as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            self.data = {}

    def __is_contact_exists(self, key) -> bool:
        return key in self.data


if __name__ == "__main__":
    addressBook = AddressBook()

    dictActions = [
        {"method": addressBook.add_record, "values": [Record("Vasya")]},
        {"method": addressBook.add_record, "values": [Record("John")]},
        {"method": addressBook.remove, "values": ["John"]},
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
