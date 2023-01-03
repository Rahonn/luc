import sys
import colorama
from colorama import Fore

import commands
import varmanager
import langs.rust
import langs.python
import langs.c
from codes.errorout import ErrorOut


mode = sys.argv[1]

commandsList = []

def modeI():
    
    with open(sys.argv[2], "r") as f:

        fileData = f.read()
        
    lines = fileData.split("\n")
    
    for line in lines:
        
        cmd = commands.getCommand(line)
        
        commandsList.append(cmd)
        
        if not cmd.run():
            
            print(f"{Fore.RED}\nError!!!{Fore.WHITE}\n")
            print(line)
            print(f"\n{Fore.BLUE}^")
            print("| Error on this line\n")
            sys.exit(0)
            
            
def modeC():
    
    lang = sys.argv[3]

    with open(sys.argv[2], "r") as f:

        fileData = f.read()

    lines = fileData.split("\n")

    for line in lines:

        cmd = commands.getCommand(line)

        commandsList.append(cmd)
        
        if type(cmd) == ErrorOut:
            print(f"{Fore.RED}\nError!!!{Fore.WHITE}\n")
            print(line)
            print(f"\n{Fore.BLUE}^")
            print("| Error on this line\n")
            sys.exit(0)

    if lang.lower() == "rust":
        
        langs.rust.toRust(commandsList)
        
    if lang.lower() == "python":

        langs.python.toPython(commandsList)
        
    if lang.lower() == "c":
        
        langs.c.toC(commandsList)
        

            
if mode.lower() == "-i":
    
    modeI()
    
if mode.lower() == "-c":
    
    modeC()
            
