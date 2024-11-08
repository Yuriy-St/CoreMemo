from .field import Field
from .custom_exceptions import InputException


class Tag(Field):
    def __init__(self, value: str):
        if not value:
            raise InputException("Tag must be not empty")

        super().__init__(value)

    def __eq__(self, other):
        return self.value == other.value