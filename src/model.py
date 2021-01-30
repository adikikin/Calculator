from state_factory import State_factory
from state import State
from i_model import I_model

class Model(I_model):
    def __init__(self):
        self.state_factory = State_factory(self)
        self.state = self.state_factory.create_state()

    def add_digit(self, digit):
        return self.state.add_digit(digit)

    def add_operator(self, operator):
        return self.state.add_operator(operator)

    def evaluate(self):
        return self.state.evaluate()

    def restart(self):
        return self.state.restart()

    def change_state(self, state):
        self.state = state