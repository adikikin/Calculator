from abc import ABC, abstractmethod
from i_state_factory import I_state_factory
from i_model import I_model
from expression import Expression

class State(ABC):
    @abstractmethod
    def __init__(self, i_state_factory, i_model):
        pass

    _expression = Expression()
    _next_state_name = None

    @abstractmethod
    def operate(self, item):
        pass
    
    @abstractmethod
    def get_next_state_name(self):
        pass
