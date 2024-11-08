from .description import Description
from .title import Title
from .tag import Tag
from .custom_exceptions import InputException


class Note:
    def __init__(self, title: str, description: str):
        self.title = Title(title)
        self.description = Description(description)
        self.tags = []

    def __str__(self):
        return f"Title: {self.title.value}, description: {self.description.value}, tags: {'; '.join(self.tags)}"

    def add_tag(self, tag: str):
        tag = Tag(tag)
        if tag in self.tags:
            raise InputException("Tag already exists")
        self.tags.append(tag)

    def remove_tag(self, tag: str):
        tag = Tag(tag)
        if tag not in self.tags:
            raise InputException("Tag does not exist")
        self.tags.remove(tag)
