import subprocess
from typing import List
from pydantic import BaseModel
import json
import os



#Class ErrorModer - Using Pydantic to create formate for the errors
#Class RunGitleaks - run gitleaks using the flags given, if there is an error to write it to the temp file. if not return True to continue the process.

class ErrorModel(BaseModel):
    exit_code: int
    error_message: str

class RunGitleaks:
    def __init__(self, args: List[str], output_file: str) -> None:
        self.output_file = output_file
        self.args = args

    def run_tool(self) -> None:
        self.result = subprocess.run(self.args, capture_output=True, text=True)

    def check_result(self, is_path_exist: bool) -> bool:
        if self.result.returncode == 0:
            self.error_message = f"Exit with status code 0"
            self.write_error_to_file(self.result.returncode, self.error_message)
            return True

        if self.result.returncode >= 1:
            if os.path.exists(self.output_file):
                return True
            elif(str(self.args[2]) != "gitleaks"):
                self.error_message = f"First argument must be 'gitleaks'"
                self.write_error_to_file(self.result.returncode, self.error_message)
                return False
            

            if "unknown flag" in self.result.stderr.lower():
                if is_path_exist:
                    self.error_message = f"Gitleaks scan failed: invalid argument '{' '.join(self.args[1:])}'"
                    self.write_error_to_file(self.result.returncode, self.error_message)
                else:
                    self.error_message = f"Gitleaks scan failed: invalid argument '{' '.join(self.args[1:-2])}'"
                    self.write_error_to_file(self.result.returncode, self.error_message)
                return False
            else:
                self.error_message = "Run without output or non existing path"
                self.write_error_to_file(self.result.returncode, self.error_message)
                return False

    def write_error_to_file(self, exit_code: int, error_message: str) -> None:
        if os.path.exists(self.output_file):
            error_data = ErrorModel(exit_code=exit_code, error_message=error_message)
            with open(self.output_file, "w") as file:
                json.dump(error_data.dict(), file, indent=4)