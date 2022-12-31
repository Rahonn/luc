from codes.basecode import Command

class Printer(Command):
    
    text = None
    
    def __init__(self, line):
        
        super().__init__(line)
        self.text = self.line[6::]
        
    def run(self):
        
        print(self.text)
        return True
    
    def get_data(self):
        
        return {
            
            "line": self.line,
            "text": self.text,
            
        }
        
    