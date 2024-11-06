from name import Name
from phone import Phone
from birthday import Birthday
from custom_exceptions import InputException


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None

    def add_phone(self, phone_str: str):
        pass

    def edit_phone(self, old_phone: str, new_phone: str):
        pass

    def remove_phone(self, phone_str: str):
        pass

    def find_phone(self, phone: str):
        pass

    def get_all_phones(self):
        pass

    def add_birthday(self, value: str):
        self.birthday = Birthday(value)

    def add_email(self, email: str):
        pass

    def edit_email(self, new_email: str):
        pass

    def remove_email(self):
        pass

    def __str__(self):
        return f"Contact name: {self.name.value}, email: {self.email}, birthday: {self.birthday}, phones: {'; '.join(p.value for p in self.phones)}"
