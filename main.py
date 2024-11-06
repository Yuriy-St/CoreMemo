def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
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
            pass
        elif command == "change_phone":
            pass
        elif command == "add_phone":
            pass
        elif command == "remove_phone":
            pass
        elif command == "add_birthday":
            pass
        elif command == "find_contact":
            pass
        elif command == "remove_contact":
            pass
        elif command == "phones":
            pass
        elif command == "show_birthday":
            pass
        elif command == "birthdays":
            pass
        elif command == "all_contacts":
            pass
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
