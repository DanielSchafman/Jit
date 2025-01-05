import sys
from typing import List
import secrets

#Class to get random file for the output_file if not given in the flags, and getting all the flags

class GetArguments:
    def __init__(self) -> None:
        if len(sys.argv) > 1:
            self.args = sys.argv[1:]
        else:
            self.args = []
        self.random_hash = secrets.token_hex(8)
        self.output_file = f"./output_{self.random_hash}.json"

    def get_output_file(self) -> str:
        if "--report-path" in self.args:
            report_path_index = self.args.index("--report-path") + 1
            if report_path_index < len(self.args):
                return self.args[report_path_index]
        return self.output_file

    def check_if_report_path_exist(self) -> bool:
        return "--report-path" in self.args

    def get_args(self) -> List[str]:
        if "--report-path" not in self.args:
            self.args.extend(["--report-path", self.output_file])
        return self.args
