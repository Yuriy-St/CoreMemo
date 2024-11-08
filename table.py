from prettytable import PrettyTable, SINGLE_BORDER


def print_table(title: str, fields: list[str], rows: list[list[str]]):
    print(title)
    table = PrettyTable()
    table.set_style(SINGLE_BORDER)
    table.field_names = fields
    table.align = "l"
    table.add_rows(rows)
    print(table)


def addressbook_commands():
    # Address book commands
    title = "Address book commands description:"
    fields = ["Command", "Description"]
    rows = [
        ["add_birthday", "Add birthday"],
        ["add_contact", "Add new contact"],
        ["add_email", "Add email"],
        ["add_phone", "Add phone number"],
        ["all_contacts", "Show all contacts"],
        ["birthdays", "Show all birthdays from particular count of days"],
        ["change_phone", "Change phone number"],
        ["edit_email", "Edit email"],
        ["find_contact", "Find contact"],
        ["remove_contact", "Remove contact"],
        ["remove_phone", "Remove phone number"],
        ["show_birthday", "Show contact birthday"],
        ["show_phones", "Show all contact phones"],
    ]

    print_table(title, fields, rows)
    print("\n")


def notebook_commands():
    title = "Note book commands description:"

    fields = ["Command", "Description"]
    rows = [
        ["add_note", "Add new note"],
        ["all_notes", "Show all notes"],
        ["edit_note", "Edit note"],
        ["find_note", "Find note"],
        ["remove_note", "Remove note"],
    ]
    print_table(title, fields, rows)
    print("\n")
