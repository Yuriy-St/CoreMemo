from src.description import Description
from src.title import Title


class Note:
    def __init__(self, title: str, description: str):
        self.title = Title(title)
        self.description = Description(description)

    def __str__(self):
        return f"Title: {self.title.value}, description: {self.description.value}"