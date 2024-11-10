from collections import UserDict

from .saveable import Saveable
from .note import Note
from .title import Title
from .description import Description
from .tag import Tag
from .custom_exceptions import RecordNotFountException


class Notes(UserDict[int, Note], Saveable):
    def __init__(self):
        super().__init__()
        Saveable.__init__(self, filename="notebook.dat")
        self.id = 1

    def _note_exists(self, id: int) -> bool:
        return id in self.data

    def get_all(self) -> dict[int, Note]:
        return self.data

    @staticmethod
    def notes_with_id(notes: dict[int, Note]) -> str:
        return "\n".join([f"id = {id} - {note}" for id, note in notes.items()])

    def __str__(self) -> str:
        return self.notes_with_id(self.data)

    def add(self, value: Note) -> int:
        note_id = self.id
        self.data[note_id] = value
        self.id += 1
        return note_id

    def add_note_tag(self, id: int, tag: str):
        if not self._note_exists(id):
            raise RecordNotFountException("Note with this id does not exist")

        self.data[id].add_tag(tag)

    def remove_note_tag(self, id: int, tag: str):
        if not self._note_exists(id):
            raise RecordNotFountException("Note with this id does not exist")

        self.data[id].remove_tag(tag)

    def search_by_text(self, query: str) -> dict[int, Note]:
        SEARCHABLE_NOTE_TEXT_FIELDS = ["title", "description"]

        result = {}
        for id, note in self.data.items():
            for field in SEARCHABLE_NOTE_TEXT_FIELDS:
                if getattr(note, field).value.lower().find(query.lower()) != -1:
                    result[id] = note
                    break

        return result

    def search_by_tag(self, value: str) -> dict[int, Note]:
        tag = Tag(value)
        result = {}
        for id, note in self.data.items():
            if tag in note.tags:
                result[id] = note

        return result

    def update_title(self, id: int, title: str):
        if not self._note_exists(id):
            raise RecordNotFountException("Note with this id does not exist")

        self.data[id].title = Title(title)

    def update_description(self, id: int, description: str):
        if not self._note_exists(id):
            raise RecordNotFountException("Note with this id does not exist")

        self.data[id].description = Description(description)

    def remove(self, id: int):
        if not self._note_exists(id):
            raise RecordNotFountException("Note with this id does not exist")

        del self.data[id]
