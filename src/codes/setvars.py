from codes.basecode import Command
import varmanager

class SetVars(Command):
    
    text = None
    name = None
    value = ""
    new = None
    
    def __init__(self, line):
        super().__init__(line)
        self.text = self.line[4::]
                    
        
    def run(self) -> bool:

        parts = self.text.split(" ")

        gettingData = False

        for partIndex in range(len(parts)):

            if partIndex == 0:

                self.name = parts[partIndex]

            if parts[partIndex] == "=":

                gettingData = True
                continue

            if gettingData:

                if partIndex == len(parts) - 1:

                    self.value = f"{self.value}{parts[partIndex]}"

                else:

                    self.value = f"{self.value}{parts[partIndex]} "
        
        try:
            
            if varmanager.vars[self.name] == None:

                self.new = True
            
            else:
                
                self.new = False
                
        except:
            
            self.new = True
            
            
        
        varmanager.vars[self.name] = str(self.value)
        
        if not gettingData:
            
            return False
        
        else:
            
            return True
            
            
    def get_data(self):
        
        return {
            
            "text": self.text,
            "name": self.name,
            "value": self.value,
            "new": self.new
            
        }
