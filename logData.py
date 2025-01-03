
import typing

class LogData:
    def __init__(self, data: dict) -> None:
        self.data = data
    
    def print_to_console(self) -> None:
        print (self.data)