from i_state_factory import I_state_factory
from i_model import I_model
from start import Start


class State_factory(I_state_factory):
    def __init__(self, i_model):
        self.i_model = i_model
        self.state_dict = {
            "Start" : Start(self, self.i_model)
            #"Error" : Error(self, self.i_model)
        }


    def create_state(self):
        return self.state_dict["Start"]
        

    def create_state_from(self, state):
        return self.state_dict[state.get_next_state_name()]