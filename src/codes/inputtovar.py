from codes.basecode import Command
import varmanager


class Input(Command):

    varname = None

    def __init__(self, line):
        super().__init__(line)
        self.varname = line[6::]
        
    def run(self) -> bool:
        varmanager.vars[self.varname] = input("")
        return True
    
    def get_data(self):
        return {
            
            "varname": self.varname,
            
        }
        


