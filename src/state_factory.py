from i_state_factory import I_state_factory
from i_model import I_model
from start import Start
from states_enum import States_enum


class State_factory(I_state_factory):
    def __init__(self, i_model):
        self.i_model = i_model
        self.state_dict = {
            States_enum.START : Start(self, self.i_model)
            # States_enum.ERROR : Error(self, self.i_model)
        }


    def create_state(self):
        return self.state_dict[States_enum.START]
        

    def create_state_from(self, state):
        enum_member = state.get_next_state_name()
        assert enum_member in self.state_dict
        return self.state_dict[enum_member]