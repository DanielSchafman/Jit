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

    def read_output_file(self) -> dict:
        if not os.path.exists(self.output_file):
            raise FileNotFoundError(f"Output file does not exist: {self.output_file}")
        
        with open(self.output_file, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                raise ValueError(f"Invalid JSON format in file: {self.output_file}")
        return data

    def process_data(self) -> Findings:
        raw_data = self.read_output_file()
    
        if isinstance(raw_data, list):
            findings_list = raw_data
        else:
            findings_list = raw_data.get("findings", [])
    
        if not findings_list:
            print("No leaks found in the output file.")
    
        findings = Findings(
            findings=[
                Leak(
                    filename=leak.get("File", "unknown"),
                    line_range=f"{leak.get('StartLine', 'unknown')}-{leak.get('EndLine', 'unknown')}",
                    description=f"Identified a pattern that may indicate {leak.get('Description', 'a potential secret.')} key"
                )
                for leak in findings_list
            ]
        )
        return findings

    def write_findings_to_file(self, findings: Findings) -> None:
        findings_dict = findings.model_dump()
        with open(self.output_file, "w") as file:
            json.dump(findings_dict, file, indent=4)
