import json
from pydantic import BaseModel

class LogData:
    def __init__(self, data: BaseModel) -> None:
        self.data = data

    def print_to_console(self) -> None:
        formatted_json = json.dumps(self.data.model_dump(), indent=4)
        print(formatted_json)
