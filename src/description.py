from field import Field
from custom_exceptions import InputException


class Description(Field):
    def __init__(self, value: str):
        if not value:
            raise InputException("Description must be not empty")

        super().__init__(value)

if __name__ == "__main__":
    for value in ["123", "abc", "0123456789", ""]:
        try:
            description = Description(value)
            print(f"Description: {description}")
        except Exception as e:
            print(f"Value: {value}, error: {e}")