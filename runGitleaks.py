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

        self.command = self.args
        self.result = subprocess.run(self.command, capture_output=True, text=True)



    
    def check_result(self) -> str:
        if self.result.returncode == 0:
            print(f"Gitleaks completed and no leaks found")
        elif self.result.returncode == 1:
            if "leaks found" in self.result.stderr.lower():
                print(f"Leaks were found during the scan:\n{self.result.stderr}")
            else:
                print(f"Gitleaks did not run as excpected Error:\n{self.result.stderr}")
                raise subprocess.CalledProcessError(
                    returncode=self.result.returncode,
                    cmd=self.command,
                    output=self.result.stdout,
                    stderr=self.result.stderr
                )
        else:
            print(f"Error running gitleaks with status code {self.result.returncode}.\n{self.result.stderr}")
            raise subprocess.CalledProcessError(
                returncode=self.result.returncode,
                cmd=self.command,
                output=self.result.stdout,
                stderr=self.result.stderr
            )        


        pass

    def get_output_file(self) -> str:
        return self.output_file
