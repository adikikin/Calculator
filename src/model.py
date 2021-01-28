from state_factory import State_factory
from state import State
from i_model import I_model

class Model(I_model):
    def __init__(self):
        self.state_factory = State_factory(self)
        self.state = self.state_factory.create_state()

    def operate(self, item):
        return self.state.operate(item)

    def change_state(self, state):
        self.state = state