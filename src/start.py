from src.state import State
from src.expression_manager import Expression_manager
from src.common import Buttons_Enum as Btns, States_enum 


class Start(State):
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
        if operator == Btns.SUB.value:
            State.expression.flip_sign()
            State.next_state_enum = States_enum.STORING_DIGITS_FOR_FIRST_OPERAND
            return_val = operator
        else:
            State.next_state_enum = States_enum.ERROR
            return_val = States_enum.ERROR.name
        State.update_model_with_next_state(self)
        return return_val


    def evaluate(self):
        return State.expression.get_operand()


    def restart(self):
        return None 
                      
