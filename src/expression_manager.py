import operator 
from src.common import Buttons_Enum as Btns
from src.infix_to_postfix_converter import Infix_to_postfix_converter
from src.expression_tree import Expression_tree, Component_Factory

#in the future: expression tree
class Expression_manager:
    def __init__(self):
        self.converter = Infix_to_postfix_converter()
        self.tree = Expression_tree()
        self.operand = 0    
        self.sign = 1
        self.infix_exp = []
        self.factory = Component_Factory()


    def reset_expression(self):
        self.operand = 0  
        self.sign = 1
        self.tree.clear_tree()
        self.infix_exp.clear() 
    

    def flip_sign(self):
        self.sign *= -1
    

    def add_digit_to_operand(self, digit):
        if self.operand == 0:
            self.operand = digit
        else:
            self.operand = self.operand * 10 + digit
        

    def get_operand(self):
        if len(self.infix_exp) == 0:
            return self.operand * self.sign
        return self.operand


    def add_operator(self, operator):
        assert operator in [i.value for i in Btns]
        assert self.operand != None
        self.infix_exp.append(self.operand)
        self.infix_exp.append(operator)
        self.operand = 0


    #may throw ZeroDivisionError exception
    def evaluate(self):
        self.infix_exp.append(self.operand)        
        postfix = self.converter.convert(self.infix_exp)
        postfix_components = [self.factory.Create_component(i) for i in postfix]
        self.tree.build_tree(postfix_components)
        self.operand = self.sign * self.tree.evaluate()
        self.sign = 1
        return self.operand
