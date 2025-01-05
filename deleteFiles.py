import os

#Class to delete the temp file in the end of the process if there is no --report-path in the flags

class DeleteFiles:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def delete_file(self) -> None:
        try:
            os.path.exists(self.file_name)
            os.remove(self.file_name)
        except Exception as e:
            print(f"Error deleting file {self.file_name}: {e}")
