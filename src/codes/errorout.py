from codes.basecode import Command

class ErrorOut(Command):
    
    def __init__(self, line):
        super().__init__(line)
        
    def run(self) -> bool:
        return False
    
    def get_data(self):
        return None
    
