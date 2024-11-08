import shlex
from src.address_book import AddressBook
from table import addressbook_commands, notebook_commands
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from src.notes import Notes
from src.commands import (
    add_birthday,
    add_contact,
    add_email,
    add_phone,
    all_contacts,
    change_phone,
    coming_birthdays,
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
    tokens = shlex.split(user_input)
    cmd, *args = tokens
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    commands = [
        "add_birthday",
        "add_contact",
        "add_email",
        "add_note",
        "add_phone",
        "all_contacts",
        "all_notes",
        "birthdays",
        "change_phone",
        "close",
        "edit_email",
        "edit_note",
        "exit",
        "find_contact",
        "find_note",
        "remove_contact",
        "remove_note",
        "remove_phone",
        "show_birthday",
        "show_phones",
    ]
    completer = WordCompleter(commands, ignore_case=True)
    session = PromptSession()

    book = AddressBook()
    print("Loading addressbook data....")
    book.load_data()

    print("\nWelcome to the assistant bot!\n")
    addressbook_commands()
    notebook_commands()
    notes = Notes()
    while True:
        user_input = session.prompt("Enter a command: ", completer=completer)
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "addressbook_commands":
            addressbook_commands()
        elif command == "notebook_commands":
            notebook_commands()
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
        elif command == "show_phones":
            print(show_phones(args, book))
        elif command == "show_birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(coming_birthdays(args, book))
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
