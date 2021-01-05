import operator 
from abc import ABC, abstractmethod


class State(ABC):
    _first_operand = 0    #in the future: expression tree
    _second_operand = 0
    _operator = ""
    _sign = 1
    _ops = {
        "+" : operator.add,
        "-" : operator.sub,
        "*" : operator.mul,
        "/" : operator.truediv,
        }
    next_state = "Start"

    @abstractmethod
    def operate(self, item):
        pass
    
    # def get_next_state(self):
    #     pass
