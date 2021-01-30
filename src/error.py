from state import State
from states_enum import States_enum

class Error(State):
    def __init__(self, i_state_factory, i_model, expression):
        self.i_factory = i_state_factory
        self.i_model = i_model


    def add_digit(self, digit):
        pass

    def add_operator(self, operator):
        pass


    def evaluate(self):
        pass


    def restart(self):
        pass
    
    def get_next_state_enum(self):
        pass

    def get_expression(self):
        pass
