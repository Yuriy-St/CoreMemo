from src.address_book import AddressBook
from src.notes import Notes
from src.commands import (
    add_birthday,
    add_contact,
    add_email,
    add_phone,
    all_contacts,
    change_phone,
    edit_email,
    find_contact,
    remove_contact,
    remove_phone,
    show_birthday,
    show_phones,
    add_note,
    all_notes,
    find_notes_by_title,
    find_notes_by_description,
    edit_note_description,
    edit_note_title,
    remove_note,
)


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    book = AddressBook()
    notes = Notes()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add_contact":
            print(add_contact(args, book))
        elif command == "change_phone":
            print(change_phone(args, book))
        elif command == "add_phone":
            print(add_phone(args, book))
        elif command == "remove_phone":
            print(remove_phone(args, book))
        elif command == "add_birthday":
            print(add_birthday(args, book))
        elif command == "add_email":
            print(add_email(args, book))
        elif command == "edit_email":
            print(edit_email(args, book))
        elif command == "find_contact":
            print(find_contact(args, book))
        elif command == "remove_contact":
            print(remove_contact(args, book))
        elif command == "phones":
            print(show_phones(args, book))
        elif command == "show_birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            pass
        elif command == "all_contacts":
            all_contacts(book)
        elif command == "add_note":
            print(add_note(args, notes))
        elif command == "edit_note_title":
            print(edit_note_title(args, notes))
        elif command == "edit_note_description":
            print(edit_note_description(args, notes))
        elif command == "remove_note":
            print(remove_note(args, notes))
        elif command == "find_notes_by_title":
            print(find_notes_by_title(args, notes))
        elif command == "find_notes_by_description":
            print(find_notes_by_description(args, notes))
        elif command == "all_notes":
            all_notes(notes)

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
