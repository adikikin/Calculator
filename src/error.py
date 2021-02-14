from src.state import State
from src.states_enum import States_enum

class Error(State):
    def __init__(self, i_state_factory, i_model, expression):
        State.i_factory = i_state_factory
        State.i_model = i_model
        State.expression = expression
        State.next_state_enum = None

    def add_digit(self, digit):
        return State.update_expression_and_model(self, 
                                                 State.expression.add_digit_to_operand,
                                                 States_enum.STORING_DIGITS_FOR_FIRST_OPERAND,
                                                 digit)


    def add_operator(self, operator):
        return States_enum.ERROR.name


    def evaluate(self):
        return States_enum.ERROR.name


    def restart(self):
        return State.update_expression_and_model(self,
                                                 State.expression.reset_expression, 
                                                 States_enum.START,
                                                 None)
 