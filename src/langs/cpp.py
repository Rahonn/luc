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
from codes.delaycmd import Delay
from codes.ifcmd import IfCmd
from codes.runifcmd import RunIfCmd
from codes.exitcmd import ExitCmd
from codes.importcmd import ImportCmd
import varmanager
import commands

def toCPP(commandsList):
    
    for cc in commandsList:

        if type(cc) == ImportCmd:

            try:

                cc.loadFile()
                cc.addToCommandList()

            except:

                print(f"{Fore.RED}\nError!!!{Fore.WHITE}\n")
                sys.exit(0)
    
    with open("output.cpp", "w") as f:
        
        f.write(toCPPFullText(commandsList))
        
    

def toCPPFullText(commandsList):
    
    print(f'{Fore.GREEN}Ignore all text in magenta!{Fore.MAGENTA}')

    output = "// Generated by LUC https://github.com/Rahonn/luc\n"

    output += f'#include <iostream>\n'
    
    mathcmdU = False
    
    for i in commandsList:

        if type(i) == MathCmd:

            output += f'#include <cmath>\n#include <string>\n'
            mathcmdU = True
            break
        
    for i in commandsList:

        if type(i) == IfCmd:

            output += f'#include <string>\n'
            mathcmdU = True
            break
        
    for i in commandsList:

        if type(i) == Delay:

            output += f'#include <ctime>\nvoid sleep(float seconds) {{\nclock_t startClock = clock();\nfloat secondsAhead = seconds * CLOCKS_PER_SEC;\nwhile (clock() < startClock + secondsAhead);\nreturn;\n}}\n'
            break
        
    output += f'int main() {{\nconst std::string VERSION = "{varmanager.vars["VERSION"]}";\n'
    
    if mathcmdU:
        
        output += "srand(time(NULL));\n"
        
        
    output += toCPPText(commandsList)
    

    output = f"{output}return 0;\n}}"

    print(Fore.RESET)
    
    return output
        


def toCPPText(commandsList):

    output = ""

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

                varmanager.vars[cc.get_data()["varname"]] = "1"

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

        if type(cc) == Delay:

            data = cc.get_data()

            output += f'sleep({float(data["time"])});\n'

        if type(cc) == CompLine:

            output += f'{cc.get_data()["code"]}\n'

        if type(cc) == IfCmd:

            data = cc.get_data()

            if not cc.run():

                print(f"{Fore.RED}\nError!!!{Fore.WHITE}\n")
                sys.exit(0)

            newdata = cc.get_data()

            trueArg1STR = False

            if not re.search(r"^[0-9]+$|^[0-9]+\.[0-9]+", str(newdata["arg1isStr"])):

                trueArg1STR = True

            trueArg2STR = False

            if not re.search(r"^[0-9]+$|^[0-9]+\.[0-9]+", str(newdata["arg2isStr"])):

                trueArg2STR = True

            if not (data["op"] == "==" and ((data["arg1isVar"] and trueArg1STR) or data["arg1isStr"]) and ((data["arg2isVar"] and trueArg2STR) or data["arg2isStr"])):

                output += f'std::string {data["varname"]};\nif ('

                if data["arg1isVar"]:

                    if not newdata["arg1isNum"]:

                        output += f'{data["arg1"][1::]}'

                    else:

                        output += f'std::stod({data["arg1"][1::]})'

                if data["arg1isStr"]:

                    output += f'"{data["arg1"][1::][:-1]}"'

                if data["arg1isNum"]:

                    output += f'{data["arg1"]}'

                output += f' {data["op"]} '

                if data["arg2isVar"]:

                    if not newdata["arg2isNum"]:

                        output += f'{data["arg2"][1::]}'

                    else:

                        output += f'std::stod({data["arg2"][1::]})'

                if data["arg2isStr"]:

                    output += f'"{data["arg2"][1::][:-1]}"'

                if data["arg2isNum"]:

                    output += f'{data["arg2"]}'

                output += ") {\n"
                output += f'{data["varname"]} = "{data["iftrue"]}";\n}}\nelse\n{{\n{data["varname"]} = "{data["iffalse"]}";\n}}\n'

            else:

                output += f'std::string {data["varname"]};\nif ('

                if data["arg1isVar"]:

                    output += f'{data["arg1"][1:]}'

                if data["arg1isStr"]:

                    output += f'"{data["arg1"][1:][:-1]}"'

                if data["arg1isNum"]:

                    output += f'{data["arg1"]}'

                output += " == "

                if data["arg2isVar"]:

                    output += f'{data["arg2"][1:]}'

                if data["arg2isStr"]:

                    output += f'"{data["arg2"][1:][:-1]}"'

                if data["arg2isNum"]:

                    output += f'{data["arg2"]}'

                output += ") {\n"
                output += f'{data["varname"]} = "{data["iftrue"]}";\n}}\nelse\n{{\n{data["varname"]} = "{data["iffalse"]}";\n}}\n'
                
        if type(cc) == RunIfCmd:

            data = cc.get_data()

            if not cc.run():

                print(f"{Fore.RED}\nError!!!{Fore.WHITE}\n")
                sys.exit(0)

            newdata = cc.get_data()

            trueArg1STR = False

            if not re.search(r"^[0-9]+$|^[0-9]+\.[0-9]+", str(newdata["arg1isStr"])):

                trueArg1STR = True

            trueArg2STR = False

            if not re.search(r"^[0-9]+$|^[0-9]+\.[0-9]+", str(newdata["arg2isStr"])):

                trueArg2STR = True

            if not (data["op"] == "==" and ((data["arg1isVar"] and trueArg1STR) or data["arg1isStr"]) and ((data["arg2isVar"] and trueArg2STR) or data["arg2isStr"])):

                output += 'if ('

                if data["arg1isVar"]:

                    if not newdata["arg1isNum"]:

                        output += f'{data["arg1"][1::]}'

                    else:

                        output += f'std::stod({data["arg1"][1::]})'

                if data["arg1isStr"]:

                    output += f'"{data["arg1"][1::][:-1]}"'

                if data["arg1isNum"]:

                    output += f'{data["arg1"]}'

                output += f' {data["op"]} '

                if data["arg2isVar"]:

                    if not newdata["arg2isNum"]:

                        output += f'{data["arg2"][1::]}'

                    else:

                        output += f'std::stod({data["arg2"][1::]})'

                if data["arg2isStr"]:

                    output += f'"{data["arg2"][1::][:-1]}"'

                if data["arg2isNum"]:

                    output += f'{data["arg2"]}'

                output += ") {\n"
                output += f'{toCPPText([commands.getCommand(data["iftrue"])])}\n}}\nelse\n{{\n{toCPPText([commands.getCommand(data["iffalse"])])}\n}}\n'

            else:

                output += 'if ('

                if data["arg1isVar"]:

                    output += f'{data["arg1"][1:]}'

                if data["arg1isStr"]:

                    output += f'"{data["arg1"][1:][:-1]}"'

                if data["arg1isNum"]:

                    output += f'{data["arg1"]}'

                output += " == "

                if data["arg2isVar"]:

                    output += f'{data["arg2"][1:]}'

                if data["arg2isStr"]:

                    output += f'"{data["arg2"][1:][:-1]}"'

                if data["arg2isNum"]:

                    output += f'{data["arg2"]}'

                output += ") {\n"
                output += f'{toCPPText([commands.getCommand(data["iftrue"])])}\n}}\nelse\n{{\n{toCPPText([commands.getCommand(data["iffalse"])])}\n}}\n'
                
        if type(cc) == ExitCmd:

            output += "return 0;"

    return output
