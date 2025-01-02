from runGitleaks import RunGitleaks
from printData import PrintData
from processData import ProcessData
from getArguments import GetArguments

if __name__=='__main__':
    args = GetArguments().get_args()
    print(f"arguments: {args}")