import constants
from field import Field
from custom_exceptions import InputException


class Email(Field):

    def __init__(self, value: str):
        if self._is_valid_value(value):
            super().__init__(value)
        else:
            raise InputException("Not valid email")

    @staticmethod
    def _is_valid_value(value: str) -> bool:
        return constants.EMAIL_REGEXP.match(value) is not None

if __name__ == "__main__":
    for value in ["groxoucrezauppou-3890@yopmail.com", "a@b.com", "0123456789", "@f.com", "sdsdgsg@com"]:
        try:
            email = Email(value)
            print(f"Email: {email}")
        except Exception as e:
            print(f"Value: {value}, error: {e}")