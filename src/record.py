from decorators import input_error
from name import Name
from phone import Phone
from birthday import Birthday
from custom_exceptions import InputException


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

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
        pass

    @input_error
    def coming_birthdays(args, book):
        days = int(args) 
        upcoming_birthdays = book.get_upcoming_birthdays(days)
        if  upcoming_birthdays:
            return "\n".join([f"{name}: {date}" for name, date in upcoming_birthdays])
        else:
            return "No birthdays within the upcoming days."
        

    @input_error
    def show_birthday(args, book):
        if len(args) < 1:
            return "Please provide a name." 
        name = args[0]
        record = book.find(name)
        if record:
            if record.birthday:
                return f"{name}'s birthday is on {record.birthday}"
            else:
                return f"No birthday set for {name}."
        else:
            return f"Contact '{name}' not found."

    def __str__(self):
        return f"Contact name: {self.name.value}, birthday: {self.birthday}, phones: {'; '.join(p.value for p in self.phones)}"
