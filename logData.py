import json
from typing import Dict
from pydantic import BaseModel

class LogData:
    def __init__(self, data: BaseModel) -> None:
        self.data = data

    def print_to_console(self) -> None:
        print(self.data.json(indent=4))