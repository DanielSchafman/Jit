from getArguments import GetArguments
from runGitleaks import RunGitleaks
from processData import ProcessData
from logData import LogData
from deleteFiles import DeleteFiles


class RunScript():

    def run_script(self):
        arg_parser = GetArguments()
        check_if_report_path_exist = arg_parser.check_if_report_path_exist()
        args = arg_parser.get_args()
        output_file = arg_parser.get_output_file()

        try:
            gitleaks_runner = RunGitleaks(args, output_file)
            gitleaks_runner.run_tool()
            gitleaks_runner.check_result()
        except Exception as e:
            print(f"Error: {e}")

        processor = ProcessData(output_file)
        try:
            structured_findings = processor.process_data()
            processor.write_findings_to_file(structured_findings)
            printer = LogData(structured_findings)
            printer.print_to_console()
            if check_if_report_path_exist is False:
                deleter = DeleteFiles(output_file,args)
                deleter.delete_file()
        except Exception as e:
            print(f"An error occurred: {e}")            
