from i_controller import i_controller
from view import View
from model import Model
from buttons_enum import Buttons_Enum

class Controller(i_controller):
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def start(self):
        self.view.show_calculator()

    def add_digit(self, digit):
        result = self.model.add_digit(digit)
        self.view.show_on_panel(result)

    def add_operator(self, operator):
        result = self.model.add_operator(operator)
        self.view.show_on_panel(result)

    def evaluate(self):
        self.view.clear_panel()
        result = self.model.evaluate() 
        if result:
            self.view.show_on_panel(result)


    def restart(self):
        assert self.model.restart() == None
        self.view.clear_panel()