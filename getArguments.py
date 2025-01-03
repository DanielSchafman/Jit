import sys
from typing import List

class GetArguments:
    def __init__(self) -> None:

        if len(sys.argv) > 1:
            self.args =(sys.argv[1:])
        else:
            self.args = ""


    def get_args(self) -> List[str]:
        return self.args
    

