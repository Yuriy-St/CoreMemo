from .decorators import input_error
from .address_book import AddressBook
from .notes import Notes
from .note import Note
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


@input_error
def add_note(args, notes: Notes):
    if len(args) == 0:
        raise ValueError("Give me title and description please.")

    if len(args) != 2:
        raise ValueError("Invalid count of arguments.")

    title, description = args

    notes.add(Note(title, description))

    return "Note added."


@input_error
def all_notes(notes: Notes):
    if len(notes.data):
        print("Notes:")
        print(notes)
    else:
        print("Empty list")


@input_error
def edit_note_title(args, notes: Notes):
    if len(args) == 0:
        raise ValueError("Give me id and title please.")

    if len(args) != 2:
        raise ValueError("Invalid count of arguments.")

    id, title = args

    if not id.isdigit():
        raise ValueError("Invalid id.")

    notes.update_title(int(id), title)

    return "Title updated."


@input_error
def edit_note_description(args, notes: Notes):
    if len(args) == 0:
        raise ValueError("Give me id and description please.")

    if len(args) != 2:
        raise ValueError("Invalid count of arguments.")

    id, description = args

    if not id.isdigit():
        raise ValueError("Invalid id.")

    notes.update_description(int(id), description)

    return "Description updated."


@input_error
def remove_note(args, notes: Notes):
    if len(args) != 1:
        raise ValueError("Invalid count of arguments.")

    (id,) = args

    if not id.isdigit():
        raise ValueError("Invalid id.")

    notes.remove(int(id))

    return "Note removed."


@input_error
def find_notes_by_title(args, notes: Notes):
    if len(args) != 1:
        raise ValueError("Invalid count of arguments.")

    (title,) = args

    notes = notes.search_by_title(title)

    if len(notes) == 0:
        return "Note not found."

    return Notes.notes_with_id(notes)


@input_error
def find_notes_by_description(args, notes: Notes):
    if len(args) != 1:
        raise ValueError("Invalid count of arguments.")

    (description,) = args

    notes = notes.search_by_description(description)

    if len(notes) == 0:
        return "Note not found."

    return Notes.notes_with_id(notes)
