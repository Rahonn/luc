import re

from codes.printer import Printer
from codes.comment import Comment, COMMENT_CHAR
from codes.errorout import ErrorOut
from codes.setvars import SetVars
from codes.printvar import PrintVar
from codes.inputtovar import Input
from codes.mathcmd import MathCmd
from codes.compline import CompLine, CODELINE_CHAR
from codes.delaycmd import Delay
from codes.ifcmd import IfCmd
from codes.runifcmd import RunIfCmd
from codes.exitcmd import ExitCmd
from codes.importcmd import ImportCmd


def getCommand(line):
    
    
    if re.search(r"^PRINT ", line, re.MULTILINE):
        
        return Printer(line)
    
    if re.search(f"^{COMMENT_CHAR}", line, re.MULTILINE) or line.strip() == "":
        
        return Comment(line)
    
    if re.search(r"^SET ", line, re.MULTILINE):
        
        return SetVars(line)
    
    if re.search(r"^PRINTVAR ", line, re.MULTILINE):
        
        return PrintVar(line)
    
    if re.search(r"^INPUT ", line, re.MULTILINE):
        
        return Input(line)
    
    if re.search(r"^MATH", line, re.MULTILINE):
        
        return MathCmd(line)
    
    if re.search(f"^{CODELINE_CHAR}", line, re.MULTILINE) or line.strip() == "":

        return CompLine(line)
    
    if re.search(r"^DELAY", line, re.MULTILINE):

        return Delay(line)
    
    
    if re.search(r"^IF", line, re.MULTILINE):
        
        return IfCmd(line)
    
    if re.search(r"^RUNIF", line, re.MULTILINE):

        return RunIfCmd(line)
    
    if re.search(r"^EXIT", line, re.MULTILINE):
        
        return ExitCmd(line)
    
    if re.search(r"^IMPORT", line, re.MULTILINE):
        
        return ImportCmd(line)
        
    
        
    return ErrorOut(line)
        
    
