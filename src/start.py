from state import State
from expression import Expression
from states_enum import States_enum
from buttons_enum import Buttons_Enum as Btns


class Start(State):
    def __init__(self, i_state_factory, i_model, expression):
        self.i_factory = i_state_factory
        self.i_model = i_model
        self.expression = expression
        self.next_state_enum = None


    def add_digit(self, digit):
        self.expression.add_digit_to_first_operand(digit)
        self.next_state_enum = States_enum.STORING_DIGITS_FOR_FIRST_OPERAND
        self.__update_model_with_new_state()
        return digit


    def add_operator(self, operator):
        if operator == Btns.SUB.value:
            self.expression.flip_sign()
            self.next_state_enum = States_enum.STORING_DIGITS_FOR_FIRST_OPERAND
            return_val = operator
        else:
            self.next_state_enum = States_enum.ERROR
            return_val = States_enum.ERROR.name
        self.__update_model_with_new_state()
        return return_val


    def evaluate(self):
        return None 


    def restart(self):
        return None 
                      

    def get_next_state_enum(self):
        return self.next_state_enum


    def get_expression(self):
        return self.expression


    def __update_model_with_new_state(self):
        new_state = self.i_factory.create_state_from(self)
        self.i_model.change_state(new_state)