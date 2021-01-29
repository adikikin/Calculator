from state import State
from states_enum import States_enum
from buttons_enum import Buttons_Enum as Btns

class Storing_digits_for_first_operand(State):
    def __init__(self, i_state_factory, i_model):
        self.i_factory = i_state_factory
        self.i_model = i_model


    def operate(self, item):
        if item in range(10):
            self._expression.add_digit_to_first_operand(item)
            State._next_state_name = States_enum.STORING_DIGITS_FOR_FIRST_OPERAND
            return_val = item   
        elif item == Btns.CLEAR.value:
            self._expression.reset_expression()
            State._next_state_name = States_enum.START
            return_val = None
        elif item == Btns.EQUAL.value:
            State._next_state_name = States_enum.STORED_OPERAND
            return_val = self._expression.get_first_operand()
        else:
            self._expression.add_operator(item)
            State._next_state_name = States_enum.STORED_OPERATOR
            return_val = item
        new_state = self.i_factory.create_state_from(self)
        self.i_model.change_state(new_state)
        return return_val

    def get_next_state_name(self):
        return self._next_state_name