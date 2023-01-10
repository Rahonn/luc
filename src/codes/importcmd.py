from codes.basecode import Command

import varmanager
import commands

class ImportCmd(Command):
    
    path = None
    truePath = None
    filedata = None
    lines = None
    commandList = None
    
    def __init__(self, line):
        super().__init__(line)
        self.path = line[7::]
        self.truePath = f'{self.path}.luc'
        
    def loadFile(self):
        
        with open(self.truePath, "r") as f:
            
            self.filedata = f.read()
            
    def addToCommandList(self):
        
        self.commandList = []
        
        self.lines = self.filedata.split("\n")
        
        for line in self.lines:
            
            cmd = commands.getCommand(line)
            
            self.commandList.append(cmd)
        
        
        cindex = varmanager.commandsList.index(self)
        
        cindex += 1
        
        for cc in self.commandList:
            
            varmanager.commandsList.insert(cindex, cc)
            
            cindex += 1
            
        
        
    def run(self) -> bool:
        try:
            
            self.loadFile()
            self.addToCommandList()
            
        except:
            
            return False
        
            
        return True
    
    
    def get_data(self):
        return {
            
            "path": self.path,
            "truePath": self.truePath,
            "filedata": self.filedata
            
            
        }
        
    
