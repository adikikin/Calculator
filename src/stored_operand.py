from src.state import State
from src.states_enum import States_enum

class Stored_operand(State):
    def __init__(self, i_state_factory, i_model, expression):
        State.i_factory = i_state_factory
        State.i_model = i_model
        State.expression = expression
        State.next_state_enum = None

    def add_digit(self, digit):
        pass


    def add_operator(self, operator):
        pass


    def evaluate(self):
        pass


    def restart(self):
        pass
 