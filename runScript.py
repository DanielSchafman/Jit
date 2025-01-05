from getArguments import GetArguments
from runGitleaks import RunGitleaks, ErrorModel
from processData import ProcessData
from logData import LogData
from deleteFiles import DeleteFiles 

#Class RunScript - Running all the functions in order

class RunScript:
    def run_script(self):
        arg_parser = GetArguments()
        check_if_report_path_exist = arg_parser.check_if_report_path_exist() 
        args = arg_parser.get_args()
        output_file = arg_parser.get_output_file()
        gitleaks_runner = RunGitleaks(args, output_file)

        try:
            gitleaks_runner.run_tool()

            if gitleaks_runner.check_result(check_if_report_path_exist):
                processor = ProcessData(output_file)
                structured_findings = processor.process_data()
                processor.write_findings_to_file(structured_findings)

                
                printer = LogData(structured_findings)
                printer.print_to_console()

                
                if not check_if_report_path_exist:
                    deleter = DeleteFiles(output_file)
                    deleter.delete_file()
            else:
                error_data = ErrorModel(exit_code=gitleaks_runner.result.returncode, error_message=gitleaks_runner.error_message)
                printer = LogData(error_data)
                printer.print_to_console() 
                deleter = DeleteFiles(output_file)
                deleter.delete_file()



        except FileNotFoundError as e:
            print(f"Error: {e}")
            gitleaks_runner.write_error_to_file(2, f"Output file not found: {output_file}")
        except Exception as e:
            print(f"Error occurred: {e}")
