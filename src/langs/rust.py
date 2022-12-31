import sys
import colorama
from colorama import Fore
import re

from codes.printer import Printer
from codes.comment import Comment, COMMENT_CHAR
from codes.errorout import ErrorOut
from codes.setvars import SetVars
from codes.printvar import PrintVar
from codes.inputtovar import Input
from codes.mathcmd import MathCmd
import varmanager

def toRust(commandsList):
    
    output = f'fn main() {{\nlet mut VERSION: &str = "{varmanager.vars["VERSION"]}";\n'

    for i in commandsList:

        if type(i) == Input:

            output = f'use std::io;\nfn main() {{\nlet mut VERSION: &str = "{varmanager.vars["VERSION"]}";\n'
            break
    
    for cc in commandsList:
        
        if type(cc) == Printer:
            
            output += f'println!("{cc.get_data()["text"]}");\n'
            
        if type(cc) == SetVars:
            
            if not cc.run():
                
                print(f"{Fore.RED}\nError!!!{Fore.WHITE}\n")
                sys.exit(0)
                
            data = cc.get_data()
            output += f'let mut {data["name"]}: &str = "{data["value"]}";\n'
            
        if type(cc) == Input:
            
            output += f'let mut {cc.get_data()["varname"]}: String = String::new();\n'
            output += f'io::stdin().read_line(&mut {cc.get_data()["varname"]}).expect("Error");\n'
            
        if type(cc) == PrintVar:
            
            output += f'println!("{{}}", {cc.get_data()["varName"]});\n'
            
        if type(cc) == MathCmd:
            
            num1 = cc.get_data()["val1"]
            num2 = cc.get_data()["val2"]
            
            if re.search(r"[0-9]", num1):
                
                num1 += ".to_string().trim()"
                
            else:
                
                num1 += ".trim()"
            
            if re.search(r"[0-9]", num2):

                num2 += ".to_string().trim()"
                
            else:

                num2 += ".trim()"
            
            if cc.get_data()["op"] == "**":

                output += f'let mut {cc.get_data()["varname"]} = f64::powf({num1}.parse::<f64>().unwrap() as f64, {num2}.parse::<f64>().unwrap() as f64);\n'

            else:

                output += f'let mut {cc.get_data()["varname"]} = {num1}.parse::<f64>().unwrap() as f64 {cc.get_data()["op"]} {num2}.parse::<f64>().unwrap() as f64;\n'
            
            
            
            
    
    output = f"{output}}}"
    
    with open("output.rs", "w") as f:
        
        f.write(output)
        
