# CoreMemo

**CoreMemo** is a command-line assistant bot designed to help you manage contacts and notes efficiently. With CoreMemo, you can store contacts with detailed information, keep track of birthdays, manage multiple phone numbers, email addresses, and handle various notes, all stored locally in JSON files for easy persistence.

## Features

CoreMemo provides the following functionalities:
- **Contact Management**:
  - Add, edit, and remove contacts.
  - Store phone numbers, email addresses, and birthdays.
  - Change or remove phone numbers and edit emails.
  - Display a list of all contacts or search for specific contacts.
  - Show contacts with upcoming birthdays.
- **Notes Management**:
  - Add, edit, remove, and search notes (functionality is currently being developed).
- **User-friendly Commands**: Enter commands through a simple CLI interface to manage your data.

## Getting Started

### Prerequisites
- **Python 3.x** is required to run CoreMemo.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Yuriy-St/CoreMemo.git
   cd CoreMemo
   ```
2. Install any necessary dependencies (if applicable).

### Usage

1. Run the assistant bot from the command line:
   ```bash
   python assistant.py
   ```
2. You will be greeted with a welcome message. Enter commands as prompted to manage your contacts and notes.

### Commands

Below are the available commands and descriptions:

#### General Commands
- `hello` - Greets the user.
- `close` or `exit` - Closes the assistant.

#### Contact Management
- `add_contact <name> <phone>` - Adds a new contact.
- `change_phone <name> <old_phone> <new_phone>` - Changes a contact’s phone number.
- `add_phone <name> <new_phone>` - Adds an additional phone number.
- `remove_phone <name> <phone>` - Removes a specific phone number.
- `add_birthday <name> <birthday>` - Adds a birthday to a contact.
- `add_email <name> <email>` - Adds an email to a contact.
- `edit_email <name> <new_email>` - Edits a contact’s email.
- `find_contact <name>` - Searches for a contact by name.
- `remove_contact <name>` - Deletes a contact.
- `phones <name>` - Shows all phone numbers for a contact.
- `show_birthday <name>` - Shows the birthday of a contact.
- `birthdays` - Show contacts with upcoming birthdays (the nearest seven days).
- `all_contacts` - Displays all contacts.

#### Notes Management
_(Coming soon)_
- `add_note <note>` - Adds a new note.
- `edit_note <note_id> <new_text>` - Edits an existing note.
- `remove_note <note_id>` - Deletes a note.
- `find_note <keyword>` - Searches for notes by keyword.
- `all_notes` - Displays all notes.

### Example

Here’s how you might interact with CoreMemo:

```plaintext
Welcome to the assistant bot!
Enter a command: hello
How can I help you?
Enter a command: add_contact John 0504444444
Contact added.
Enter a command: all_contacts
Contact name: John, phones: 0504444444
Enter a command: show_birthday John
Birthday: 10.12.1990
Enter a command: close
Good bye!
```

### Data Storage

All contacts and notes are stored in JSON files within the `data/` directory. This ensures that your data is preserved between sessions.

## Contributing

Contributions are welcome! If you’d like to add features or improve functionality, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

---

Let me know if there’s any additional functionality or information you’d like to include!
