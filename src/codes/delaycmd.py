import time

from codes.basecode import Command

class Delay(Command):
    
    time = None
    
    def __init__(self, line):
        super().__init__(line)
        self.time = line[6::]
    
    def run(self) -> bool:
        
        try:
            
            time.sleep(float(self.time))
            
        except:
            
            return False
        
        return True
    

    def get_data(self):
        
        return {
            
            "time": self.time
            
        }
