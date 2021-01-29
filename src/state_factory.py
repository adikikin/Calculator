from storing_digits_for_first_operand import Storing_digits_for_first_operand
from storing_digits_for_second_operand import Storing_digits_for_second_operand
from stored_operator import Stored_operator
from stored_operand import Stored_operand
from i_state_factory import I_state_factory
from states_enum import States_enum
from expression import Expression
from i_model import I_model
from start import Start
from error import Error

class State_factory(I_state_factory):
    def __init__(self, i_model):
        self.i_model = i_model
        self.state_dict = {
            States_enum.START : Start,
            States_enum.ERROR : Error,
            States_enum.STORED_OPERATOR:Stored_operator,
            States_enum.STORED_OPERAND: Stored_operand,
            States_enum.STORING_DIGITS_FOR_FIRST_OPERAND: Storing_digits_for_first_operand,
            States_enum.STORING_DIGITS_FOR_SECOND_OPERAND: Storing_digits_for_second_operand,
        }


    def create_state(self):
        return self.state_dict[States_enum.START](self, self.i_model, Expression())
        

    def create_state_from(self, state):
        enum_member = state.get_next_state_enum()
        assert enum_member in self.state_dict
        return self.state_dict[enum_member](self, self.i_model, state.get_expression())