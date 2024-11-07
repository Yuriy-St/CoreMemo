from src.address_book import AddressBook
from prettytable import PrettyTable
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
)


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!\n")
    print("Address book commands description:\n")
    addressBookCommndsDescription = PrettyTable()
    addressBookCommndsDescription.field_names = ["Command", "Description"]
    addressBookCommndsDescription.add_rows(
        [
            ["add_contact", "Add new contact"],
            ["change_phone", "Change phone number"],
            ["add_phone", "Add phone number"],
            ["remove_phone", "Remove phone number"],
            ["add_birthday", "Add birthday"],
            ["add_email", "Add email"],
            ["edit_email", "Edit email"],
            ["find_contact", "Find contact"],
            ["remove_contact", "Remove contact"],
            ["show_phones", "Show all contact phones"],
            ["show_birthday", "Show contact birthday"],
            ["birthdays", "Show all birthdays from particular count of days"],
            ["all_contacts", "Show all contacts"],
        ]
    )
    print(addressBookCommndsDescription)
    print("\nNote book commands description:\n")
    noteBookCommndsDescription = PrettyTable()
    noteBookCommndsDescription.field_names = ["Command", "Description"]
    noteBookCommndsDescription.add_rows(
        [
            ["add_note", "Add new note"],
            ["edit_note", "Edit note"],
            ["remove_note", "Remove note"],
            ["find_note", "Find note"],
            ["all_notes", "Show all notes"],
        ]
    )
    print(noteBookCommndsDescription)
    print("\n")
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
        elif command == "show_phones":
            print(show_phones(args, book))
        elif command == "show_birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            pass
        elif command == "all_contacts":
            all_contacts(book)
        elif command == "add_note":
            pass
        elif command == "edit_note":
            pass
        elif command == "remove_note":
            pass
        elif command == "find_note":
            pass
        elif command == "all_notes":
            pass

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
