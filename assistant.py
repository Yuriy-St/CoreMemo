import shlex
from src.address_book import AddressBook
from src.table import addressbook_commands, notebook_commands
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
    find_notes_by_text,
    edit_note_description,
    edit_note_title,
    remove_note,
    add_note_tag,
    remove_note_tag,
    find_notes_by_tag,
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
        "add_note_tag",
        "add_phone",
        "all_contacts",
        "all_notes",
        "birthdays",
        "change_phone",
        "close",
        "edit_email",
        "edit_note_description",
        "edit_note_title",
        "exit",
        "find_contact",
        "find_notes_by_tag",
        "find_notes_by_text",
        "remove_contact",
        "remove_note",
        "remove_note_tag",
        "remove_phone",
        "show_birthday",
        "show_phones",
    ]
    completer = WordCompleter(commands, ignore_case=True)
    session = PromptSession()

    book = AddressBook()
    notes = Notes()
    print("Loading saved data....")
    book.load_data()
    notes.load_data()

    print("\nWelcome to the assistant bot!\n")
    addressbook_commands()
    notebook_commands()
    while True:
        user_input = session.prompt("Enter a command: ", completer=completer)

        match parse_input(user_input):
            case ["close"] | ["exit"]:
                print("Good bye!")
                break
            case ["hello"]:
                print("How can I help you?")
            case ["addressbook_commands"]:
                addressbook_commands()
            case ["notebook_commands"]:
                notebook_commands()
            case ["add_contact", *args]:
                print(add_contact(args, book))
            case ["change_phone", *args]:
                print(change_phone(args, book))
            case ["add_phone", *args]:
                print(add_phone(args, book))
            case ["remove_phone", *args]:
                print(remove_phone(args, book))
            case ["add_birthday", *args]:
                print(add_birthday(args, book))
            case ["add_email", *args]:
                print(add_email(args, book))
            case ["edit_email", *args]:
                print(edit_email(args, book))
            case ["find_contact", *args]:
                find_contact(args, book)
            case ["remove_contact", *args]:
                print(remove_contact(args, book))
            case ["show_phones", *args]:
                show_phones(args, book)
            case ["show_birthday", *args]:
                show_birthday(args, book)
            case ["birthdays", *args]:
                print(coming_birthdays(args, book))
            case ["all_contacts", *args]:
                all_contacts(book)
            case ["add_note", *args]:
                print(add_note(args, notes))
            case ["edit_note_title", *args]:
                print(edit_note_title(args, notes))
            case ["edit_note_description", *args]:
                print(edit_note_description(args, notes))
            case ["remove_note", *args]:
                print(remove_note(args, notes))
            case ["find_notes_by_tag", *args]:
                find_notes_by_tag(args, notes)
            case ["find_notes_by_text", *args]:
                find_notes_by_text(args, notes)
            case ["add_note_tag", *args]:
                print(add_note_tag(args, notes))
            case ["remove_note_tag", *args]:
                print(remove_note_tag(args, notes))
            case ["all_notes", *args]:
                all_notes(notes)
            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
