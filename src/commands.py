import re

from codes.printer import Printer
from codes.comment import Comment, COMMENT_CHAR
from codes.errorout import ErrorOut
from codes.setvars import SetVars
from codes.printvar import PrintVar
from codes.inputtovar import Input
from codes.mathcmd import MathCmd
from codes.compline import CompLine, CODELINE_CHAR

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
    
        
    return ErrorOut(line)
        
    
