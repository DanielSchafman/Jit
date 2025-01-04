from getArguments import GetArguments
from runGitleaks import RunGitleaks
from processData import ProcessData
from logData import LogData
from deleteFiles import DeleteFiles


class RunScript():
    def __init__(self, output_file):
        self.output_file = output_file

    def run_script(self):
        args = GetArguments().get_args()    
        try:
            gitleaks_runner = RunGitleaks(args, self.output_file)
            gitleaks_runner.run_tool()
            gitleaks_runner.check_result()
        except Exception as e:
            print(f"Error: {e}")

        processor = ProcessData(self.output_file)
        try:
            structured_findings = processor.process_data()
            printer = LogData(structured_findings)
            printer.print_to_console()
            deleter = DeleteFiles(self.output_file)
            deleter.delete_file()
        except Exception as e:
            print(f"An error occurred: {e}")            
