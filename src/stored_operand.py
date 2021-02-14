from src.state import State
from src.states_enum import States_enum

class Stored_operand(State):
    def __init__(self, i_state_factory, i_model, expression):
        State.i_factory = i_state_factory
        State.i_model = i_model
        State.expression = expression
        State.next_state_enum = None

    def add_digit(self, digit):
        State.expression.reset_expression()
        return State.update_expression_and_model(self, 
                                                 State.expression.add_digit_to_operand, 
                                                 States_enum.STORING_DIGITS_FOR_FIRST_OPERAND,
                                                 digit)


    def add_operator(self, operator):
        return State.update_expression_and_model(self, 
                                                 State.expression.add_operator, 
                                                 States_enum.STORED_OPERATOR,
                                                 operator)
    


    def evaluate(self):
        return State.expression.get_first_operand()
         


    def restart(self):
        return State.update_expression_and_model(self,
                                                 State.expression.reset_expression, 
                                                 States_enum.START,
                                                 None)

 