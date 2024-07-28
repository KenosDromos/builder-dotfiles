import json
from typing import Any


# ______________________________________________________________________ Json
class Json:
    """A class for managing a Json file"""

    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_file(self) -> Any:
        with open(self.file_path, 'r', encoding="utf-8") as file:
            return json.load(file)
    
    def write_file(self, data: dict) -> None:
        with open(self.file_path, 'w', encoding="utf-8") as file:
            json.dump(data, file, indent = 4)



# ______________________________________________________________________ AnyFile
class AnyFile:
    pass