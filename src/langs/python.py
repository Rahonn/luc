import sys
import colorama
from colorama import Fore
import re

from codes.printer import Printer
from codes.setvars import SetVars
from codes.printvar import PrintVar
from codes.inputtovar import Input
from codes.mathcmd import MathCmd
from codes.compline import CompLine
import varmanager

def toPython(commandsList):
    
    output = f'VERSION = "{varmanager.vars["VERSION"]}"\n'
    
    for cc in commandsList:
        
        if type(cc) == Printer:
            
            output += f'print("{cc.get_data()["text"]}")\n'
            
        if type(cc) == SetVars:
            
            if not cc.run():

                print(f"{Fore.RED}\nError!!!{Fore.WHITE}\n")
                sys.exit(0)
            
            data = cc.get_data()
            
            output += f'{data["name"]} = "{data["value"]}"\n'
            
        if type(cc) == PrintVar:
            
            output += f'print({cc.get_data()["varName"]})\n'
            
        if type(cc) == Input:
            
            output += f'{cc.get_data()["varname"]} = input()\n'
            
        if type(cc) == MathCmd:
            
            data = cc.get_data()
            
            output += f'{data["varname"]} = float({data["val1"]}) {data["op"]} float({data["val2"]})\n'
            
        if type(cc) == CompLine:
            
            output += f'{cc.get_data()["code"]}\n';
            
    with open("output.py", "w") as f:
        
        f.write(output)
        
