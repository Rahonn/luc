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


def toCPP(commandsList):

    output = f'#include <iostream>\nint main() {{\nconst char VERSION[] = "{varmanager.vars["VERSION"]}";\n'
    
    for i in commandsList:

        if type(i) == MathCmd:

            output = f'#include <iostream>\n#include <cmath>\n#include <string>\nint main() {{\nconst std::string VERSION = "{varmanager.vars["VERSION"]}";\nsrand(time(NULL));\n'
            break

    for cc in commandsList:

        if type(cc) == Printer:

            output += f'std::cout << "{cc.get_data()["text"]}" << \'\\n\';\n'

        if type(cc) == SetVars:

            if not cc.run():

                print(f"{Fore.RED}\nError!!!{Fore.WHITE}\n")
                sys.exit(0)

            data = cc.get_data()
            
            
            if data["new"] == True:
                
                output += f'std::string {data["name"]} = "{data["value"]}";\n'
                
            else:
                
                output += f'{data["name"]} = "{data["value"]}";\n'
                
                

        if type(cc) == Input:

            if varmanager.vars.get(cc.get_data()["varname"]) is None:
                
                output += f'std::string {cc.get_data()["varname"]};\n'
                output += f'std::getline(std::cin, {cc.get_data()["varname"]});\n'
                
                varmanager.vars[cc.get_data()["varname"]] = True
                
            else:
                
                print(f"{Fore.RED}\nError!!!{Fore.WHITE}\n")
                sys.exit(0)
                

        if type(cc) == PrintVar:

            output += f'std::cout << {cc.get_data()["varName"]} << \'\\n\';\n'

        if type(cc) == MathCmd:

            num1 = cc.get_data()["val1"]
            num2 = cc.get_data()["val2"]
            
            if not re.search(r"[0-9]", num1):

                num1 = f"std::stod({num1})"
                
            
            if not re.search(r"[0-9]", num2):

                num2 = f"std::stod({num2})"
                
            if varmanager.vars.get(cc.get_data()["varname"]) is None:
                
                varmanager.vars[cc.get_data()["varname"]] = True
            
                if cc.get_data()["op"] == "**":

                    output += f'std::string {cc.get_data()["varname"]} = std::to_string(pow({num1}, {num2}));\n'
                    
                elif cc.get_data()["op"] == "RAND" and cc.get_data()["val1"] == "@" and cc.get_data()["val2"] == "@":
                    
                    output += f'std::string {cc.get_data()["varname"]} = std::to_string(rand());\n'
                    
                elif cc.get_data()["op"] == "RAND" and not cc.get_data()["val1"] == "@" and not cc.get_data()["val2"] == "@":

                    output += f'std::string {cc.get_data()["varname"]} = std::to_string((int) rand() % (int) {num2} + (int) {num1});\n'

                else:

                    output += f'std::string {cc.get_data()["varname"]} = std::to_string({num1} {cc.get_data()["op"]} {num2});\n'
            
            else:
                
                print(f"{Fore.RED}\nError!!!{Fore.WHITE}\n")
                sys.exit(0)
                
        if type(cc) == CompLine:

            output += f'{cc.get_data()["code"]}\n'

    output = f"{output}return 0;\n}}"

    with open("output.cpp", "w") as f:
        
        f.write(output)
