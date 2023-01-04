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


def toC(commandsList):

    output = f'#include <stdio.h>\n#include <string.h>\nint main() {{\nconst char VERSION[] = "{varmanager.vars["VERSION"]}";\n'
    
    for i in commandsList:

        if type(i) == MathCmd:

            output = f'#include <stdio.h>\n#include <math.h>\n#include <string.h>\n#include <stdlib.h>\nint main() {{\nconst char VERSION[] = "{varmanager.vars["VERSION"]}";\nchar *eptr;\n'
            break

    for cc in commandsList:

        if type(cc) == Printer:

            output += f'printf("{cc.get_data()["text"]}\\n");\n'

        if type(cc) == SetVars:

            if not cc.run():

                print(f"{Fore.RED}\nError!!!{Fore.WHITE}\n")
                sys.exit(0)

            data = cc.get_data()
            
            
            if data["new"] == True:
                
                output += f'char {data["name"]}[] = "{data["value"]}";\n'
                
            else:
                
                output += f'strcpy({data["name"]}, "{data["value"]}");\n'
                
                

        if type(cc) == Input:

            if varmanager.vars.get(cc.get_data()["varname"]) is None:
                
                output += f'char {cc.get_data()["varname"]}[25];\n'
                output += f'fgets({cc.get_data()["varname"]}, 25, stdin);\n'
                
                varmanager.vars[cc.get_data()["varname"]] = True
                
            else:
                
                print(f"{Fore.RED}\nError!!!{Fore.WHITE}\n")
                sys.exit(0)
                

        if type(cc) == PrintVar:

            output += f'printf("%s\\n", {cc.get_data()["varName"]});\n'

        if type(cc) == MathCmd:

            num1 = cc.get_data()["val1"]
            num2 = cc.get_data()["val2"]
            
            if not re.search(r"[0-9]", num1):

                num1 = f"strtod({num1}, &eptr)"
                
            
            if not re.search(r"[0-9]", num2):

                num2 = f"strtod({num2}, &eptr)"
                
            if varmanager.vars.get(cc.get_data()["varname"]) is None:
                
                varmanager.vars[cc.get_data()["varname"]] = True
            
                if cc.get_data()["op"] == "**":

                    output += f'char {cc.get_data()["varname"]}[25];\nsnprintf({cc.get_data()["varname"]}, 25, \"%lf\", pow({num1}, {num2}));\n'

                else:

                    output += f'char {cc.get_data()["varname"]}[25];\nsnprintf({cc.get_data()["varname"]}, 25, \"%lf\", {num1} {cc.get_data()["op"]} {num2});\n'
            
            else:
                
                print(f"{Fore.RED}\nError!!!{Fore.WHITE}\n")
                sys.exit(0)
                
        if type(cc) == CompLine:

            output += f'{cc.get_data()["code"]}\n'

    output = f"{output}return 0;\n}}"

    with open("output.c", "w") as f:
        
        f.write(output)
