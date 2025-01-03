from getArguments import GetArguments
from runGitleaks import RunGitleaks
from processData import ProcessData
from logData import LogData


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
        data = processor.read_output_file()
        data_transformed = processor.transform_data(data)
        printer = LogData(data_transformed)
        printer.print_to_console()
