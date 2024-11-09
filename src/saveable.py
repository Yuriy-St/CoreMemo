import pickle

from pathlib import Path


class Saveable:

    def __init__(self, filename: str):
        data_folder = Path("data")
        if not data_folder.exists():
            data_folder.mkdir()
        self.file = data_folder / Path(filename)

    def save_data(self):
        with self.file.open("wb") as file:
            pickle.dump(self, file)

    def load_data(self):
        try:
            with self.file.open("rb") as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            self.data = {}
