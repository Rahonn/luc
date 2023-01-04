import sys
import colorama
from colorama import Fore

import commands
import varmanager
import langs.rust
import langs.python
import langs.c
import langs.cpp
from codes.errorout import ErrorOut


mode = sys.argv[1]


def modeI():
    
    commandsList = []
    
    with open(sys.argv[2], "r") as f:

        fileData = f.read()
        
    lines = fileData.split("\n")
    
    for line in lines:
        
        cmd = commands.getCommand(line)
        
        commandsList.append(cmd)
        
        if not cmd.run():
            
            print(f"{Fore.RED}\nError!!!{Fore.RESET}\n")
            print(line)
            print(f"\n{Fore.BLUE}^")
            print("| Error on this line\n")
            sys.exit(0)
            
            
            
def modeC(lin):
    
    commandsList = []
    
    lang = lin

    with open(sys.argv[2], "r") as f:

        fileData = f.read()

    lines = fileData.split("\n")

    for line in lines:

        cmd = commands.getCommand(line)

        commandsList.append(cmd)
        
        if type(cmd) == ErrorOut:
            print(f"{Fore.RED}\nError!!!{Fore.RESET}\n")
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
        
    if lang.lower() == "c++":

        langs.cpp.toCPP(commandsList)
        
    print(f"{Fore.BLUE}Compiled!{Fore.RESET}")
        

def modeD():
    
    print(f"{Fore.BLUE}Running code...{Fore.GREEN}\n")
    modeI()
    varmanager.vars = varmanager.defaultvars
    print(f"{Fore.BLUE}")
    isgood = input("Is this ok? (y or n): ")
    if isgood == "y":
        
        cancomp = input("Do you want to complie this? (y or n): ")
        
        if cancomp == "y":
            
            print(f"\t{Fore.CYAN}LANGS")
            print("Type python for Python")
            print("Type rust for Rust")
            print("Type c for C")
            print(f"Type c++ for C++{Fore.BLUE}")
            
            complang = input("Enter the lang to compile in: ")
            
            modeC(complang)
        
        else:
            
            print(f"Goodbye!{Fore.RESET}")
    
    else:
        
        print(f"Goodbye!{Fore.RESET}")
        
    

            
if mode.lower() == "-i":
    
    modeI()
    
if mode.lower() == "-c":
    
    modeC(sys.argv[3])

if mode.lower() == "-d":
    
    modeD()
