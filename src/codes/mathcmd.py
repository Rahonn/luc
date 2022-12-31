from codes.basecode import Command
import varmanager

import re

class MathCmd(Command):
    
    lineNOSTART = None
    varname = None
    op = None
    val1 = None
    val2 = None
    
    def __init__(self, line):
        super().__init__(line)
        self.lineNOSTART = self.line[5::]
        
        self.varname = self.lineNOSTART.split(" ")[0]
        self.op = self.lineNOSTART.split(" ")[1]
        self.val1 = self.lineNOSTART.split(" ")[2]
        self.val2 = self.lineNOSTART.split(" ")[3]
        
        
    def run(self) -> bool:
            
        try:

            num1 = self.val1
            num2 = self.val2

            if re.search(r"[^0-9]", self.val1):

                num1 = float(varmanager.vars[self.val1])

            if re.search(r"[^0-9]", self.val2):

                num2 = float(varmanager.vars[self.val2])

            num1 = float(num1)
            num2 = float(num2)

            if self.op == "+":

                varmanager.vars[self.varname] = num1 + num2

            elif self.op == "-":

                varmanager.vars[self.varname] = num1 - num2

            elif self.op == "/":

                varmanager.vars[self.varname] = num1 / num2

            elif self.op == "*":

                varmanager.vars[self.varname] = num1 * num2

            elif self.op == "%":

                varmanager.vars[self.varname] = num1 % num2

            elif self.op == "**":

                varmanager.vars[self.varname] = num1 ** num2

            else:

                return False

            return True

        except:

            return False
            
        
    
    def get_data(self):
        return {
            
            "lineNOSTART": self.lineNOSTART,
            "varname": self.varname,
            "op": self.op,
            "val1": self.val1,
            "val2": self.val2,
            
        }
    


