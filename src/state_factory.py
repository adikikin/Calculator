from storing_digits_for_first_operand import Storing_digits_for_first_operand
from storing_digits_for_second_operand import Storing_digits_for_second_operand
from storing_operator import Storing_operator
from storing_operand import Storing_operand
from i_state_factory import I_state_factory
from states_enum import States_enum
from i_model import I_model
from start import Start
from error import Error


class State_factory(I_state_factory):
    def __init__(self, i_model):
        self.i_model = i_model
        self.state_dict = {
            States_enum.START : Start(self, self.i_model),
            States_enum.ERROR : Error(self, self.i_model),
            States_enum.STORING_OPERATOR:Storing_operator(self, self.i_model),
            States_enum.STORING_OPERAND: Storing_operand(self, self.i_model),
            States_enum.STORING_DIGITS_FOR_FIRST_OPERAND: Storing_digits_for_first_operand(self, self.i_model),
            States_enum.STORING_DIGITS_FOR_SECOND_OPERAND: Storing_digits_for_second_operand(self, self.i_model),
        }


    def create_state(self):
        return self.state_dict[States_enum.START]
        

    def create_state_from(self, state):
        enum_member = state.get_next_state_name()
        assert enum_member in self.state_dict
        return self.state_dict[enum_member]