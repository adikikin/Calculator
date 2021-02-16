from src.common import Buttons_Enum as btn
from collections import deque


class Infix_to_postfix_converter:
    def __init__(self):
        self.precedency_dict = {btn.MUL.value : 2,
                                btn.DIV.value : 2,
                                btn.ADD.value : 1,
                                btn.SUB.value : 1
                               }
        self.ops_stack = deque() #operatorrs stack


    def __get_precedency(self, item):
            return self.precedency_dict[item]


    def __move_item_from_ops_stack_to_result_exp(self, postfix_exp):
        op = self.ops_stack.pop()
        postfix_exp.append(op)


    def __move_higher_and_equal_precedency_ops_to_result_exp(self, operator, postfix_exp):
        while len(self.ops_stack) > 0 and self.__get_precedency(self.ops_stack[-1]) >= self.__get_precedency(operator):
            self.__move_item_from_ops_stack_to_result_exp(postfix_exp)
    

    def convert(self, expression):
        assert len(expression) > 2
        result = []
        for item in expression:
            if item in self.precedency_dict:
                self.__move_higher_and_equal_precedency_ops_to_result_exp(item, result)
                self.ops_stack.append(item)
            else:
                assert type(item) == int or type(item) == float
                result.append(item)
        while self.ops_stack:
            self.__move_item_from_ops_stack_to_result_exp(result)
        return result

