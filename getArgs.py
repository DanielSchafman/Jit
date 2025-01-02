import sys
from typing import List

class GetArgs:
    def __init__(self) -> None:

        if len(sys.argv) > 1:
            self.args = " ".join(sys.argv[1:])
        else:
            self.args = ""


    def get_args(self) -> str:
        return self.args
    

