from src.record import Record
from src.decorators import input_error
from src.address_book import AddressBook

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

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

    name, = args

    record = book.find(name)

    return record

@input_error
def remove_contact(args, book: AddressBook):
    if len(args) != 1:
        raise ValueError("Invalid count of arguments.")

    name, = args

    book.remove(name)

    return "Contact removed."

@input_error
def show_birthday(args, book: AddressBook):
    if len(args) != 1:
        raise ValueError("Invalid count of arguments.")

    name, = args

    record = book.find(name)

    return f"Birthday: {record.birthday}"

@input_error
def show_phones(args, book: AddressBook):
    if len(args) != 1:
        raise ValueError("Invalid count of arguments.")

    name, = args

    record = book.find(name)

    return f"Phones: {'; '.join(p.value for p in record.get_all_phones())}"

def main():
    book = AddressBook()
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
            if len(book.data) > 0:
                print("Contacts:")
                for name, record in book.data.items():
                    print(record)
            else:
                print("Empty list")
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
