from state import State
from states_enum import States_enum

class Storing_operand(State):
    def __init__(self, i_state_factory, i_model):
        self.i_factory = i_state_factory
        self.i_model = i_model


    def operate(self, item):
        pass


    def get_next_state_name(self):
        pass
        # return self._next_state_name