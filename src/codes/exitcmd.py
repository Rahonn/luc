import sys

from codes.basecode import Command


class ExitCmd(Command):
    
    def __init__(self, line):
        super().__init__(line)
        
    def run(self) -> bool:
        sys.exit(0)
        return True
    
    def get_data(self):
        return super().get_data()
    
