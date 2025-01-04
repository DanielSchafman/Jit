import json
import os
from pydantic import BaseModel
from typing import List

class Leak(BaseModel):
    filename: str
    line_range: str
    description: str

class Findings(BaseModel):
    findings: List[Leak]

class ProcessData:
    def __init__(self, output_file: str) -> None:
        self.output_file = output_file

    def read_output_file(self) -> List[dict]:
        if not os.path.exists(self.output_file):
            raise FileNotFoundError(f"Output file does not exist: {self.output_file}")

        with open(self.output_file, "r") as file:
            data = json.load(file)
        return data

    def process_data(self) -> Findings:
        raw_data = self.read_output_file()
        findings = Findings(
            findings=[
                Leak(
                    filename=leak["File"],
                    line_range=f"{leak['StartLine']}-{leak['EndLine']}",
                    description=f"Identified a pattern that may indicate {leak.get('Description', 'a potential secret.')} key"
                )
                for leak in raw_data
            ]
        )
        return findings
