from address_book import AddressBook
from decorators import input_error


@input_error
def show_phone(args, book: AddressBook):  
    # Показує номер телефону для вказаного контакту.
    if len(args) < 1:
        return "Please provide a name." 
    name = args[0]
    record = book.find(name)
    if record:
        phones = ', '.join(phone.value for phone in record.phones)
        return f"{name}'s phone numbers are: {phones}"
    else:
        return f"Contact {name} not found."
    

@input_error
def show_all(book: AddressBook): 
    # Показує всі контакти.  
    if book.data:
        return "Contacts:\n" + "\n".join(str(record) for record in book.data.values())
    else:
        return "No contacts found."
    
    
@input_error
def birthdays(args, book):
    days = int(args) 
    upcoming_birthdays = book.get_upcoming_birthdays(days)
    if  upcoming_birthdays:
        return "\n".join([f"{name}: {date}" for name, date in upcoming_birthdays])
    else:
        return "No birthdays within the upcoming days."


@input_error
def show_birthday(args, book):
    if len(args) < 1:
        return "Please provide a name." 
    name = args[0]
    record = book.find(name)
    if record:
        if record.birthday:
            return f"{name}'s birthday is on {record.birthday}"
        else:
            return f"No birthday set for {name}."
    else:
        return f"Contact '{name}' not found."
    


@input_error
def add_birthday(args, book):
    if len(args) < 2:
        return "Please provide both name and birthday in the format: [name] [DD.MM.YYYY]"
    name, birthday = args[0], args[1]
    record = book.find(name)
    if record:
        try:
            record.set_birthday(birthday)
            return f"Birthday for {name} added successfully."
        except ValueError as e:
            return str(e)  # Виведе повідомлення про неправильний формат дати
    else:
        return f"Contact '{name}' not found."