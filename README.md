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

#### Address Book Commands

The Address Book module allows you to manage and search contacts. Here are the available commands:

| Command                                      | Description                                          |
|----------------------------------------------|------------------------------------------------------|
| `add_birthday <name> <birthday>`             | Add a birthday to a contact                          |
| `add_contact <name> <phone>`                 | Add a new contact with a phone number                |
| `add_email <name> <email>`                   | Add an email address to a contact                    |
| `add_phone <name> <phone>`                   | Add an additional phone number to an existing contact |
| `all_contacts`                               | Show all contacts                                    |
| `birthdays <nearest_days_number>`            | Show all birthdays within the next specified days    |
| `change_phone <name> <old_phone> <new_phone>`| Update an existing phone number                      |
| `edit_email <name> <new_email>`              | Update an email address                              |
| `find_contact <name>`                        | Search for a contact by name                         |
| `remove_contact <name>`                      | Remove a contact                                     |
| `remove_phone <name> <phone>`                | Remove a phone number from a contact                 |
| `show_birthday <name>`                       | Show the birthday of a specific contact              |
| `show_phones <name>`                         | Show all phone numbers for a specific contact        |

#### Note Book Commands

The Note Book module allows you to add, edit, and organize notes with ease. Here are the available commands:

| Command                                       | Description                |
|-----------------------------------------------|----------------------------|
| `add_note <title> <description>`              | Add a new note             |
| `add_note_tag <note_id> <tag>`                | Add a tag to a note        |
| `all_notes`                                   | Display all notes          |
| `edit_note_title <note_id> <new_title>`       | Edit the title of a note   |
| `edit_note_description <note_id> <new_description>` | Edit the description of a note |
| `find_notes_by_text <query>`                  | Search notes by text       |
| `find_notes_by_tag <tag>`                     | Search notes by tag        |
| `remove_note <note_id>`                       | Delete a note              |
| `remove_note_tag <note_id> <tag>`             | Remove a tag from a note   |

### Example

Here’s how you might interact with CoreMemo:

```plaintext
Welcome to the assistant bot!
Enter a command: hello
How can I help you?
Enter a command: add_contact John 0506789123
Contact added.
Enter a command: all_contacts
Contacts:
┌──────────────┬──────────────┬────────────┬────────────┐
│ Contact name │ Email        │ Birthday   │ Phones     │
├──────────────┼──────────────┼────────────┼────────────┤
│ Bob          │ bob@mail.com │ 10.11.1990 │ 1234567890 │
│              │              │            │ 0981234567 │
├──────────────┼──────────────┼────────────┼────────────┤
│ Alice        │              │ 13.11.1995 │ 0987654321 │
├──────────────┼──────────────┼────────────┼────────────┤
│ John         │              │            │ 0506789123 │
└──────────────┴──────────────┴────────────┴────────────┘
Enter a command: show_birthday Bob
┌──────────────┬────────────┐
│ Contact name │ Birthday   │
├──────────────┼────────────┤
│ Bob          │ 10.11.1990 │
└──────────────┴────────────┘
Enter a command: close
Good bye!
```

### Data Storage

All contacts and notes are stored in the `*.dat` files within the `data/` directory. This ensures that your data is preserved between sessions.

## Contributing

Contributions are welcome! If you’d like to add features or improve functionality, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

---

Let us know if there’s any additional functionality or information you’d like to include!
