from getArguments import GetArguments
from runGitleaks import RunGitleaks

if __name__ == '__main__':
    # Step 1: Get arguments using GetArguments
    args = GetArguments().get_args()
    
    # Step 2: Define the output file path
    output_file = "/home/daniel/Desktop/Devops/Jit/output.json"  # Adjust this path as needed

    # Step 3: Initialize and run Gitleaks
    try:
        gitleaks_runner = RunGitleaks(args, output_file)
        gitleaks_runner.run_tool()
        gitleaks_runner.check_result()
    except Exception as e:
        print(f"Error: {e}")
