import constants
from field import Field
from datetime import datetime
from custom_exceptions import InputException


class Birthday(Field):
    def __init__(self, value):
        super().__init__(self.__convert_to_datetime(value))

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")

    def __convert_to_datetime(self, value):
        try:

            if not constants.DATE_REGEXP.match(value):
                raise InputException

            date = datetime.strptime(value, '%d.%m.%Y')

            return date
        except InputException:
            raise InputException("Invalid date format. Use DD.MM.YYYY")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


if __name__ == "__main__":
    for value in ["10.12.2022", "", "10.", "1.2.2002", "2222"]:
        try:
            birthday = Birthday(value)
            print(f"birthday: {birthday}")
        except Exception as e:
            print(f"Value: {value}, error: {e}")