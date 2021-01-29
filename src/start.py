from state import State
from states_enum import States_enum
from buttons_enum import Buttons_Enum as Btns


class Start(State):
    def __init__(self, i_state_factory, i_model):
        self.i_factory = i_state_factory
        self.i_model = i_model


    def operate(self, item):
        State._expression.reset_expression()
        if item in [Btns.EQUAL.value, Btns.CLEAR.value]: #"=", "C"
            State._next_state_name = States_enum.START
            return_val = None               
        elif item in [Btns.MUL.value, Btns.DIV.value, Btns.ADD.value]:
            State._next_state_name = States_enum.ERROR
            return_val = States_enum.ERROR.name
        else:
            if item == Btns.SUB.value:
                State._expression.flip_sign()
            else:
                State._expression.add_digit_to_first_operand(item)
            State._next_state_name = States_enum.STORING_DIGITS_FOR_FIRST_OPERAND
            return_val = item
        new_state = self.i_factory.create_state_from(self)
        self.i_model.change_state(new_state)
        return return_val


    def get_next_state_name(self):
        return self._next_state_name