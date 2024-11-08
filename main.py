from src.address_book import AddressBook
from table import addressbook_commands, notebook_commands
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
    print("\nWelcome to the assistant bot!\n")
    addressbook_commands()
    notebook_commands()

    while True:
        user_input = input("Enter a command: ")
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
