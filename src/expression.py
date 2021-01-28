import operator 
from buttons_enum import Buttons_Enum as Btns

#in the future: expression tree
class Expression:
    def __init__(self):
        self.first_operand = 0    
        self.second_operand = 0
        self.operator = None
        self.sign = 1
        self.ops = {
            Btns.ADD.value : operator.add,
            Btns.SUB.value : operator.sub,
            Btns.MUL.value : operator.mul,
            Btns.DIV.value : operator.truediv,
            }
    
    def reset_expression(self):
        self.first_operand = 0  
        self.second_operand = 0
        self.operator = None
        self.sign = 1
    
    def flip_sign(self):
        self.sign *= -1
    
    def add_digit_to_first_operand(self, digit):
        if self.first_operand == 0:
            self.first_operand = digit
        else:
            self.first_operand *= 10 
            self.first_operand += digit

    #def operate(self):
