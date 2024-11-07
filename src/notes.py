from collections import UserDict
from .note import Note
from .title import Title
from .description import Description
from .custom_exceptions import RecordNotFountException


class Notes(UserDict[int, Note]):
    def __init__(self):
        super().__init__()
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

    def add(self, value: Note):
        self.data[self.id] = value
        self.id += 1

    def _search_by(self, key: str, query: str) -> dict[int, Note]:
        return { id: note for id, note in self.data.items() if getattr(note, key).value.lower().find(query.lower()) != -1 }

    def search_by_title(self, title: str) -> dict[int, Note]:
        return self._search_by("title", title)
    
    def search_by_description(self, description: str) -> dict[int, Note]:
        return self._search_by("description", description)
        
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