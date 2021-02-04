import operator 
from src.buttons_enum import Buttons_Enum as Btns

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
    

    def __add_digit(self, operand, digit):
        if operand == 0:
            operand = digit
        else:
            operand = operand * 10 + digit
        return operand

    def add_digit_to_first_operand(self, digit):
        self.first_operand = self.__add_digit(self.first_operand, digit)

    def add_digit_to_second_operand(self, digit):
        self.second_operand = self.__add_digit(self.second_operand, digit)

    def get_first_operand(self):
        return self.first_operand * self.sign

    #may throw ZeroDivisionError exception
    def add_operator(self, operator):
        assert operator in self.ops
        if self.second_operand != 0:
            assert self.operator != None
            self.evaluate()
        self.operator = operator
        

    #may throw ZeroDivisionError exception
    def evaluate(self):
        assert self.operator in self.ops
        self.first_operand = self.sign * self.ops[self.operator](self.first_operand, self.second_operand)
        self.sign = 1
        return self.first_operand
