import subprocess
from typing import List
import os

class RunGitleaks:
    def __init__(self, args: List[str], output_file: str = "./output.json") -> None:
        self.output_file = output_file
        self.args =  args

        if "--report-path" not in args:
            self.args += ["--report-path", self.output_file]

    def run_tool(self) -> None:
        self.result = subprocess.run(self.args, capture_output=True, text=True)

    def check_result(self) -> None:

        if self.result.returncode == 0:
            print(f"Gitleaks completed successfully. Output written to: {self.output_file}")
            if not os.path.exists(self.output_file):
                print(f"Error: Output file was not created at {self.output_file}.")
        elif self.result.returncode == 1:
            if "leaks found" in (self.result.stderr.lower() or self.result.stdout.lower()):
                print(f"Leaks were found during the scan. Check the report at: {self.output_file}")
            else:
                print(f"Gitleaks did not run as expected. Error: {self.result.stderr or self.result.stdout}")
        else:
            print(f"Gitleaks scan failed: {self.result.stderr or self.result.stdout}")

    def get_output_file(self) -> str:
        return self.output_file
