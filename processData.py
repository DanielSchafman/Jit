import json
from typing import List
import os

class ProcessData:
    def __init__(self, output_file: str) -> None:
        self.output_file = output_file

    def read_output_file(self) -> dict:
        if not os.path.exists(self.output_file):
            raise FileExistsError(f"Output file dose not exist: {self.output_file}")
        
        with open(self.output_file, "r") as file:
            data = json.load(file)
            return data
        
        
    def transform_data(self, data: List[dict]) -> dict:
        findings = []
        for leak in data:
            findings.append({
                "filename": leak.get("File", "unknown"),
                "line_range": f"{leak.get('StartLine', 'unknown')}-{leak.get('EndLine', 'unknown')}",
                "description": leak.get("Description", "No description provided.")
            })
        return {"findings": findings}