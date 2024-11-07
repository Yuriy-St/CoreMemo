from .decorators import input_error
from .address_book import AddressBook
from .record import Record


@input_error
def add_contact(args, book: AddressBook):
    if len(args) == 0:
        raise ValueError("Give me name and phone please.")

    if len(args) != 2:
        raise ValueError("Invalid count of arguments.")

    name, phone = args

    john_record = Record(name)
    john_record.add_phone(phone)
    book.add_record(john_record)

    return "Contact added."


@input_error
def change_phone(args, book: AddressBook):
    if len(args) == 0:
        raise ValueError("Give me name and phones please.")

    if len(args) != 3:
        raise ValueError("Invalid count of arguments.")

    name, old_phone, new_phone = args

    record = book.find(name)
    record.edit_phone(old_phone, new_phone)

    return "Phone changed."


@input_error
def add_phone(args, book: AddressBook):
    if len(args) == 0:
        raise ValueError("Give me name and phone please.")

    if len(args) != 2:
        raise ValueError("Invalid count of arguments.")

    name, phone = args

    record = book.find(name)
    record.add_phone(phone)

    return "Phone added."


@input_error
def all_contacts(book: AddressBook):
    if len(book.data):
        print("Contacts:")
        for record in book.data.values():
            print(record)
    else:
        print("Empty list")


@input_error
def remove_phone(args, book: AddressBook):
    if len(args) == 0:
        raise ValueError("Give me name and phone please.")

    if len(args) != 2:
        raise ValueError("Invalid count of arguments.")

    name, phone = args

    record = book.find(name)
    record.remove_phone(phone)

    return "Phone removed."


@input_error
def add_birthday(args, book: AddressBook):
    if len(args) == 0:
        raise ValueError("Give me name and birthday please.")

    if len(args) != 2:
        raise ValueError("Invalid count of arguments.")

    name, birthday = args

    record = book.find(name)
    record.add_birthday(birthday)

    return "Birthday added."


@input_error
def add_email(args, book: AddressBook):
    if len(args) == 0:
        raise ValueError("Give me name and email please.")

    if len(args) != 2:
        raise ValueError("Invalid count of arguments.")

    name, email = args

    record = book.find(name)
    record.add_email(email)

    return "Email added."


@input_error
def edit_email(args, book: AddressBook):
    if len(args) == 0:
        raise ValueError("Give me name and email please.")

    if len(args) != 2:
        raise ValueError("Invalid count of arguments.")

    name, email = args

    record = book.find(name)
    record.edit_email(email)

    return "Email added."


@input_error
def find_contact(args, book: AddressBook):
    if len(args) != 1:
        raise ValueError("Invalid count of arguments.")

    (name,) = args

    record = book.find(name)

    return record


@input_error
def remove_contact(args, book: AddressBook):
    if len(args) != 1:
        raise ValueError("Invalid count of arguments.")

    (name,) = args

    book.remove(name)

    return "Contact removed."


@input_error
def show_birthday(args, book: AddressBook):
    if len(args) != 1:
        raise ValueError("Invalid count of arguments.")

    (name,) = args

    record = book.find(name)

    return f"Birthday: {record.birthday}"


@input_error
def show_phones(args, book: AddressBook):
    if len(args) != 1:
        raise ValueError("Invalid count of arguments.")

    (name,) = args

    record = book.find(name)

    return f"Phones: {'; '.join(p.value for p in record.get_all_phones())}"
