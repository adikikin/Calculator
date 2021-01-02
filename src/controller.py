from i_controller import i_controller
from view import View

class Controller(i_controller):
    def __init__(self):
        #self.model = Model()
        self.view = View()

    def start(self):
        pass

    def add_digit(self, digit):
        pass

    def add_operator(self, operator):
        pass

    def evaluate(self):
        pass

    def restart(self):
        pass
