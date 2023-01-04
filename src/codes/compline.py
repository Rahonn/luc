from codes.basecode import Command

CODELINE_CHAR = '!'

class CompLine(Command):
    
    code = None
    
    def __init__(self, line):
        super().__init__(line)
        self.code = line[1::]
        
        
    def run(self):
        return True
    
    def get_data(self):
        return {
            
            "code": self.code
            
        }
    

