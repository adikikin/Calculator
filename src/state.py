from abc import ABC, abstractmethod
from i_state_factory import I_state_factory
from i_model import I_model

class State(ABC):
    @abstractmethod
    def __init__(self, i_state_factory, i_model, expression):
        pass

    # @abstractmethod
    # @classmethod
    # def create_from(cls, state)


    @abstractmethod
    def add_digit(self, digit):
        pass

    @abstractmethod
    def add_operator(self, operator):
        pass

    @abstractmethod
    def evaluate(self):
        pass

    @abstractmethod
    def restart(self):
        pass
    
    @abstractmethod
    def get_next_state_enum(self):
        pass

    @abstractmethod
    def get_expression(self):
        pass