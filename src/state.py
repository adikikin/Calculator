from abc import ABC, abstractmethod
from i_state_factory import I_state_factory
from i_model import I_model

class State(ABC):
    @abstractmethod
    def __init__(self, i_state_factory, i_model, expression):
        self.i_factory = i_state_factory
        self.i_model = i_model
        self.expression = expression
        self.next_state_enum = None


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
    
    def get_next_state_enum(self):
        return self.next_state_enum


    def get_expression(self):
        return self.expression


    def update_expression_and_model(self,
                                    expression_func, 
                                    next_state_enum, item=None):
        if item == None:
            expression_func()
        else:
            expression_func(item)
        self.next_state_enum = next_state_enum
        self.update_model_with_next_state()
        return item


    def update_model_with_next_state(self):
        new_state = self.i_factory.create_state_from(self)
        self.i_model.change_state(new_state)
