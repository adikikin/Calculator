from state import State
from states_enum import States_enum

class Start(State):
    def __init__(self, i_state_factory, i_model):
        self.i_factory = i_state_factory
        self.i_model = i_model


    def operate(self, item):
        self.__reset_expression()
        if item in ["=", "C"]:
            State._next_state_name = States_enum.START
            return_val = None               
        elif item in ["x", "/", "+"]:
            return_val = State._next_state_name = States_enum.ERROR
        else:
            if item == "-":
                State._sign *= -1
            State._next_state_name = States_enum.STORING_DIGITS_FOR_FIRST_OPERAND
            return_val = item
        new_state = self.i_factory.create_state_from(States_enum.START)
        self.i_model.change_state(new_state)
        return return_val


    def __reset_expression(self):
        State._first_operand = 0  
        State._second_operand = 0
        State._operator = ""
        State._sign = 1


    def get_next_state_name(self):
        return self._next_state_name