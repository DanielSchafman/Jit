import os

class DeleteFiles:
    def __init__(self, file_name: str, args: list[str]) -> None:
        self.file_name = file_name
        self.args = args


    def delete_file(self) -> None:
        if os.path.exists(self.file_name):
            os.remove(self.file_name)