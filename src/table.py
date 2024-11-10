from prettytable import PrettyTable, SINGLE_BORDER, ALL
from colorama import Fore


def print_table(
    title: str, fields: list[str], rows: list[list[str]], hrules: bool = False
):
    print(title) if title else print("")
    table = PrettyTable()
    table.set_style(SINGLE_BORDER)
    if hrules:
        table.hrules = ALL
    table.field_names = fields
    table.align = "l"
    table.add_rows(rows)
    print(table)


def addressbook_commands():
    # Address book commands
    title = "Address book commands description:"
    fields = ["Command", "Description"]
    rows = [
        [
            f"{Fore.BLUE}add_birthday {Fore.YELLOW}<name> <birthday>{Fore.RESET}",
            "Add birthday",
        ],
        [
            f"{Fore.BLUE}add_contact {Fore.YELLOW}<name> <phone>{Fore.RESET}",
            "Add new contact",
        ],
        [f"{Fore.BLUE}add_email {Fore.YELLOW}<name> <email>{Fore.RESET}", "Add email"],
        [
            f"{Fore.BLUE}add_phone {Fore.YELLOW}<name> <phone>{Fore.RESET}",
            f"Add phone number to the existing contact",
        ],
        [f"{Fore.BLUE}all_contacts{Fore.RESET}", "Show all contacts"],
        [
            f"{Fore.BLUE}birthdays {Fore.YELLOW}<nearest_days_number>{Fore.RESET}",
            f"Show all birthdays from particular count of days",
        ],
        [
            f"{Fore.BLUE}change_phone {Fore.YELLOW}<name> <old_phone> <new_phone>{Fore.RESET}",
            f"Change phone number",
        ],
        [
            f"{Fore.BLUE}edit_email {Fore.YELLOW}<name> <new_email>{Fore.RESET}",
            "Edit email",
        ],
        [f"{Fore.BLUE}find_contact {Fore.YELLOW}<name>{Fore.RESET}", "Find contact"],
        [
            f"{Fore.BLUE}remove_contact {Fore.YELLOW}<name>{Fore.RESET}",
            "Remove contact",
        ],
        [
            f"{Fore.BLUE}remove_phone {Fore.YELLOW}<name> <phone>{Fore.RESET}",
            "Remove phone number",
        ],
        [
            f"{Fore.BLUE}show_birthday {Fore.YELLOW}<name>{Fore.RESET}",
            "Show contact birthday",
        ],
        [
            f"{Fore.BLUE}show_phones {Fore.YELLOW}<name>{Fore.RESET}",
            "Show all contact phones",
        ],
    ]

    print_table(title, fields, rows)
    print("\n")


def notebook_commands():
    title = "Note book commands description:"

    fields = ["Command", "Description"]
    rows = [
        [
            f"{Fore.BLUE}add_note {Fore.YELLOW}<title> <description>{Fore.RESET}",
            "Add new note",
        ],
        [
            f"{Fore.BLUE}add_note_tag {Fore.YELLOW}<note_id> <tag>{Fore.RESET}",
            "Add note tag",
        ],
        [f"{Fore.BLUE}all_notes{Fore.RESET}", "Show all notes"],
        [
            f"{Fore.BLUE}edit_note_title {Fore.YELLOW}<note_id> <new_title>{Fore.RESET}",
            "Edit note title",
        ],
        [
            f"{Fore.BLUE}edit_note_description {Fore.YELLOW}<note_id> <new_description>{Fore.RESET}",
            "Edit note description",
        ],
        [
            f"{Fore.BLUE}find_notes_by_text {Fore.YELLOW}<query>{Fore.RESET}",
            "Find notes by text",
        ],
        [
            f"{Fore.BLUE}find_notes_by_tag {Fore.YELLOW}<tag>{Fore.RESET}",
            "Find notes by tag",
        ],
        [f"{Fore.BLUE}remove_note {Fore.YELLOW}<note_id>{Fore.RESET}", "Remove note"],
        [
            f"{Fore.BLUE}remove_note_tag {Fore.YELLOW}<note_id> <tag>{Fore.RESET}",
            "Remove note tag",
        ],
    ]
    print_table(title, fields, rows)
    print("\n")
