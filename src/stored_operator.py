from src.state import State
from src.states_enum import States_enum

class Stored_operator(State):
    def __init__(self, i_state_factory, i_model, expression):
        State.i_factory = i_state_factory
        State.i_model = i_model
        State.expression = expression
        State.next_state_enum = None

    def add_digit(self, digit):
        return State.update_expression_and_model(self, 
                                                 State.expression.add_digit_to_operand, 
                                                 States_enum.STORING_DIGITS_FOR_SECOND_OPERAND,
                                                 digit)


    def add_operator(self, operator):
        State.update_expression_and_model(self, 
                                          State.expression.reset_expression, 
                                          States_enum.ERROR,
                                          None)
        return States_enum.ERROR.name
        

    def evaluate(self):
        #same functionallity as add_operator- state changes to ERROR
        return self.add_operator(None) 


    def restart(self):
        return State.update_expression_and_model(self,
                                                 State.expression.reset_expression, 
                                                 States_enum.START,
                                                 None)

 