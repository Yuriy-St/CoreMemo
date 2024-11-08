from .name import Name
from .email import Email
from .phone import Phone
from .birthday import Birthday
from .custom_exceptions import InputException


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones: list = []
        self.birthday = None
        self.email = None

    def add_phone(self, phone_str: str):
        if self.find_phone(phone_str):
            raise InputException("This phone has already exists for current user")

        phone = Phone(phone_str)

        self.phones.append(phone)

    def edit_phone(self, old_phone: str, new_phone: str):
        phone = self.find_phone(old_phone)

        if not phone:
            raise InputException("This phone not exists for current user")

        self.phones[self.phones.index(phone)] = Phone(new_phone)

    def remove_phone(self, phone_str: str):
        phone = self.find_phone(phone_str)

        if not phone:
            raise InputException(
                "Couldn't remove this phone. Phone not exists for current user"
            )

        self.phones.remove(phone)

    def find_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                return p

        return None

    def get_all_phones(self):
        return self.phones

    def add_birthday(self, value: str):
        self.birthday = Birthday(value)

    def add_email(self, email: str):
        self.email = Email(email)

    def edit_email(self, new_email: str):
        if self.email is None:
            raise InputException("Please firstly add email to this contact")

        if self.email.value == new_email:
            raise InputException("Emails are same")

        self.email = Email(new_email)

    def remove_email(self):
        self.email = None

  

    def __str__(self):
        return f"Contact name: {self.name.value}, email: {self.email}, birthday: {self.birthday}, phones: {'; '.join(p.value for p in self.phones)}"


if __name__ == "__main__":
    record = Record("Vasya")
    print(record)

    dictActions = [
        {"method": record.add_phone, "values": ["1111111111"]},
        {"method": record.add_phone, "values": ["1111111113"]},
        {"method": record.edit_phone, "values": ["1111111111", "1111111112"]},
        {"method": record.remove_phone, "values": ["1111111112"]},
        {"method": record.add_birthday, "values": ["11.11.2020"]},
        {"method": record.edit_email, "values": ["groxoucrezauppou-3890@yopmail.com"]},
        {"method": record.add_email, "values": ["groxoucrezauppou-3890@yopmail.com"]},
        {"method": record.edit_email, "values": ["groxoucrezauppou-3890@yopmail.com"]},
        {"method": record.edit_email, "values": ["groxoucrezauppou-3891@yopmail.com"]},
    ]

    for item in dictActions:
        try:
            values = item["values"]
            item["method"].__call__(*values)
            print(record)
        except Exception as e:
            print(f"Values: {values}, error: {e}")
