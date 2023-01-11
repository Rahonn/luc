from codes.basecode import Command

class PassCmd(Command):
    
    def __init__(self, line):
        super().__init__(line)
        
    def run(self) -> bool:
        return True
    
    def get_data(self):
        return None
    
    
