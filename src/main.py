import sys
import colorama
from colorama import Fore

import commands
import varmanager
import langs.python
import langs.c
import langs.cpp
from codes.errorout import ErrorOut



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

    
    didComp = False
    
    if lang.lower() == "python":

        didComp = True

        langs.python.toPython(commandsList)
        
    if lang.lower() == "c":
        
        didComp = True
        
        langs.c.toC(commandsList)
        
    if lang.lower() == "c++":
        
        didComp = True

        langs.cpp.toCPP(commandsList)
        
    if didComp:
        
        print(f"{Fore.BLUE}Compiled!{Fore.RESET}")
        
    else:
        
        print(f"{Fore.RED}Unknowen Error!")
        
        

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
            print("Type c for C")
            print(f"Type c++ for C++{Fore.BLUE}")
            
            complang = input("Enter the lang to compile in: ")
            
            modeC(complang)
        
        else:
            
            print(f"Goodbye!{Fore.RESET}")
    
    else:
        
        print(f"Goodbye!{Fore.RESET}")
        
    
def modeH():
    
    print(f"\t{Fore.CYAN}Code Help{Fore.RESET}")
    print(f"{Fore.BLUE}Print\t-\tTo print something out\t-\tPRINT [string]")
    print("Print Var\t-\tTo print a var out\t-\tPRINTVAR [varname]")
    print("Set\t-\tTo set a var\t-\tSET [varname] = [value]")
    print("Input\t-\tTo get user input\t-\tINPUT [varname]")
    print("Math\t-\tOperators +, -, *, /, **, RAND and store the result to a new var. If you are using RAND you can make num1 and num2 @ for no set range\t-\tMATH [varname] [operator] [num1] [num2]")
    print("Delay\t-\tAdd a delay to your code\t-\tDELAY [seconds]")
    print("Comments\t-\tUse # for comments\t-\t# [comment]")
    print("Compline\t-\tDoes not run in interpretation but gets added to main function in compilation\t-\t![line]")
    print("If\t-\tAn if system. Replace varname with the name of the outvar, replace args with the args use for string with this put a ! at the start and end and if you are using a var as a arg put a $ at the start of it's name\t-\tIF [varname] [arg1] [op] [arg2] :[outiftrue]:[outiffalse]:")
    print(
        "Run If\t-\tAn if system. Replace args with the args use for string with this put a ! at the start and end and if you are using a var as a arg put a $ at the start of it's name, replace [outcmdiftrue] with the command to run if the if is true same for the [outcmdiffalse] but for false instead\t-\tIF [varname] [arg1] [op] [arg2] |[outcmdiftrue]|[outcmdiffalse]|")
    print()
    print(f"\t{Fore.RED}Comands Options{Fore.RESET}")
    print(f"{Fore.MAGENTA}Interpret\t-\tTo run code\t-\t./LUC -i [filename]")
    print("Compile\t-\tTo compile to output src. You can compile to c, c++ and python\t-\t./LUC -c [filename] [lang]")
    print("Debug\t-\tInterprets and Compiles your code\t-\t./LUC -d [filename]")
    print("Playground\t-\tEnter the code playground\t-\t./LUC -p")
    print("Help\t-\tTo get this info\t-\t./LUC --help")
    print(f"Version\t-\tTo get the LUC version number\t-\t./LUC --version{Fore.RESET}")
    modeV()

def modeV():
    
    print(f'{Fore.LIGHTGREEN_EX}LUC version: {varmanager.vars["VERSION"]}{Fore.RESET}')
    
def modeP():
    
    print(f"{Fore.LIGHTCYAN_EX}Starting playground...")
    print(f"{Fore.LIGHTBLUE_EX}At any time type $exit to quit")
    
    print(f"{Fore.MAGENTA}Welcome to the playground!")
    print()
    
    while True:
        
        line = input(f"{Fore.GREEN}>>> ")
        
        if line == "$exit":
            
            print(f"{Fore.MAGENTA}Goodbye!")
            sys.exit(0)
            
        
        cmd = commands.getCommand(line)
        
        print(Fore.MAGENTA, end="")
        if not cmd.run():
            
            print(f"{Fore.RED}Thats a error!")
            
        

if len(sys.argv) <= 1:
    
    modeH()
    sys.exit(0)

mode = sys.argv[1]
            
if mode.lower() == "-i":
    
    modeI()
    
if mode.lower() == "-c":
    
    modeC(sys.argv[3])

if mode.lower() == "-d":
    
    modeD()

if mode.lower() == "--help" or mode.lower() == "-help" or mode.lower() == "-h":
    
    modeH()
    
if mode.lower() == "--version" or mode.lower() == "-version" or mode.lower() == "-v":

    modeV()
    
if mode.lower() == "-p":
    
    modeP()
