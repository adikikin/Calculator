from src.state import State
from src.common import States_enum
from src.common import Buttons_Enum as Btns

class Storing_digits_for_first_operand(State):
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
        return State.update_expression_and_model(self, 
                                                 State.expression.add_operator, 
                                                 States_enum.STORED_OPERATOR,
                                                 operator)
        
    def restart(self):
        return State.update_expression_and_model(self,
                                                 State.expression.reset_expression, 
                                                 States_enum.START,
                                                 None)


    def evaluate(self):
        State.next_state_enum = States_enum.STORED_OPERAND
        State.update_model_with_next_state(self)
        return State.expression.get_operand()
