import operator 
from abc import ABC, abstractmethod
from i_state_factory import I_state_factory
from i_model import I_model

class State(ABC):
    @abstractmethod
    def __init__(self, i_state_factory, i_model):
        pass
    
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
    _next_state_name = None

    @abstractmethod
    def operate(self, item):
        pass
    
    @abstractmethod
    def get_next_state_name(self):
        pass
