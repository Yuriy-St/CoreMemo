from src.field import Field
from custom_exceptions import InputException

class Title(Field):
    def __init__(self, value: str):
        if not value:
            raise InputException("Title must be not empty")

        super().__init__(value)

if __name__ == "__main__":
    for value in ["123", "abc", "0123456789", ""]:
        try:
            title = Title(value)
            print(f"Title: {title}")
        except Exception as e:
            print(f"Value: {value}, error: {e}")