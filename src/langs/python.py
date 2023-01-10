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
import varmanager
import commands


def toPython(commandsList):
    
    with open("output.py", "w") as f:
        
        f.write(toPythonFullText(commandsList))
        
    

def toPythonFullText(commandsList):
    
    print(f'{Fore.GREEN}Ignore all text in magenta!{Fore.MAGENTA}')
    
    output = '# Generated by LUC https://github.com/Rahonn/luc\n'
    
    
    for i in commandsList:

        if type(i) == MathCmd:

            output += 'import random\n'
            break
    
    for i in commandsList:

        if type(i) == Delay:

            output += 'import time\n'
            break

    output += f'VERSION = "{varmanager.vars["VERSION"]}"\n'

    
    output += toPythonText(commandsList)

        
    print(Fore.RESET)
    
    
    return output
    
        

def toPythonText(commandsList):

    output = ''

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

            varmanager.vars[cc.get_data()["varname"]] = "1"

        if type(cc) == MathCmd:

            data = cc.get_data()

            if data["val1"] == "@" and data["val2"] == "@" and data["op"] == "RAND":

                output += f'{data["varname"]} = random.random()\n'
                varmanager.vars[cc.get_data()["varname"]] = True

            elif not data["val1"] == "@" and not data["val2"] == "@" and data["op"] == "RAND":

                output += f'{data["varname"]} = random.randint(int({data["val1"]}), int({data["val2"]}))\n'
                varmanager.vars[cc.get_data()["varname"]] = True

            else:

                output += f'{data["varname"]} = float({data["val1"]}) {data["op"]} float({data["val2"]})\n'
                varmanager.vars[cc.get_data()["varname"]] = True

        if type(cc) == Delay:

            data = cc.get_data()

            output += f'time.sleep({data["time"]})\n'

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

                output += f'{data["varname"]} = "{data["iftrue"]}" if '

                if data["arg1isVar"]:

                    if not newdata["arg1isNum"]:

                        output += f'{data["arg1"][1::]}'

                    else:

                        output += f'float({data["arg1"][1::]})'

                if data["arg1isStr"]:

                    output += f'"{data["arg1"][1::][:-1]}"'

                if data["arg1isNum"]:

                    output += f'{data["arg1"]}'

                output += f' {data["op"]} '

                if data["arg2isVar"]:

                    output += data["arg2"][1:]

                if data["arg2isStr"]:

                    output += f'"{data["arg2"][1::][:-1]}"'

                if data["arg2isNum"]:

                    output += f'{data["arg2"]}'

                output += f' else "{data["iffalse"]}"\n'

            else:

                output += f'{data["varname"]} = "{data["iftrue"]}" if '

                if data["arg1isVar"]:

                    output += f'str({data["arg1"][1:]})'

                if data["arg1isStr"]:

                    output += f'"{data["arg1"][1:][:-1]}"'

                if data["arg1isNum"]:

                    output += f'{data["arg1"]}'

                output += f' {data["op"]} '

                if data["arg2isVar"]:

                    output += f'str({data["arg2"][1:]})'

                if data["arg2isStr"]:

                    output += f'"{data["arg2"][1:][:-1]}"'

                if data["arg2isNum"]:

                    output += f'{data["arg2"]}'

                output += f' else "{data["iffalse"]}"\n'
                
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

                output += f'if '

                if data["arg1isVar"]:

                    if not newdata["arg1isNum"]:

                        output += f'{data["arg1"][1::]}'

                    else:

                        output += f'float({data["arg1"][1::]})'

                if data["arg1isStr"]:

                    output += f'"{data["arg1"][1::][:-1]}"'

                if data["arg1isNum"]:

                    output += f'{data["arg1"]}'

                output += f' {data["op"]} '

                if data["arg2isVar"]:

                    output += data["arg2"][1:]

                if data["arg2isStr"]:

                    output += f'"{data["arg2"][1::][:-1]}"'

                if data["arg2isNum"]:

                    output += f'{data["arg2"]}'

                output += f':\n    {toPythonText([commands.getCommand(data["iftrue"])])}\nelse:\n    {toPythonText([commands.getCommand(data["iffalse"])])}\n'

            else:

                output += f'if '

                if data["arg1isVar"]:

                    output += f'str({data["arg1"][1:]})'

                if data["arg1isStr"]:

                    output += f'"{data["arg1"][1:][:-1]}"'

                if data["arg1isNum"]:

                    output += f'{data["arg1"]}'

                output += f' {data["op"]} '

                if data["arg2isVar"]:

                    output += f'str({data["arg2"][1:]})'

                if data["arg2isStr"]:

                    output += f'"{data["arg2"][1:][:-1]}"'

                if data["arg2isNum"]:

                    output += f'{data["arg2"]}'

                output += f':\n    {toPythonText([commands.getCommand(data["iftrue"])])}\nelse:\n    {toPythonText([commands.getCommand(data["iffalse"])])}\n'
                
        if type(cc) == ExitCmd:

            output += "quit()"

    return output 
