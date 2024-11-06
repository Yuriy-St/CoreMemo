import constants
from field import Field
from custom_exceptions import InputException


class Phone(Field):

    def __init__(self, value: str):
        if self._is_valid_value(value):
            super().__init__(value)
        else:
            raise InputException("The phone number must consist of only 10 digits")

    @staticmethod
    def _is_valid_value(value: str) -> bool:
        return constants.PHONE_REGEXP.match(value) is not None


if __name__ == "__main__":
    for value in ["123", "abc", "0123456789"]:
        try:
            phone = Phone(value)
            print(f"Phone number: {phone}")
        except Exception as e:
            print(f"Value: {value}, error: {e}")
