import subprocess
from typing import List


# init - define the arguments
# run_tool - run the gitleaks using subprocess library
# get_output_file - returns the output of gitleaks

class RunGitleaks:
    def __init__(self, args: List[str], output_file: str) -> None:
        self.args = args
        self.output_file = output_file


    def run_tool(self) -> None:
        command = ["gitleaks"] + self.args + ["--report-path", self.output_file]
        try:
            subprocess.run(command, check=True)

        except subprocess.CalledProcessError as e:
            print(f"Error running gitleaks: {e}")
            raise

    
    def get_output_file(self) -> str:
        return self.output_file
