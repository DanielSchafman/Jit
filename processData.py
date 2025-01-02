import json
from typing import List, Dict

class ProcessData:
    def __init__(self, output_file: str) -> None:
        self.output_file = output_file

    def load_data(self) -> Dict:
        try:
            with open (self.output_file, "r") as file:
                data = json.load(file)
                return data
        except FileNotFoundError as e:
            print(f"Error {self.output_file} not found")
            raise e
        
        except json.JSONDecodeError as e:
            print(f"Error to parse to JSON from '{self.output_file}'")
            raise e
        
    def transform_data(self, raw_data: Dict) -> Dict:
        pass