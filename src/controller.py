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
        result = self.model.operate(digit)
        self.view.show_on_panel(result)

    def add_operator(self, operator):
        pass

    def evaluate(self):
        self.view.clear_panel()
        result = self.model.operate(Buttons_Enum.EQUAL.value) 
        if result:
            self.view.show_on_panel(result)


    def restart(self):
        assert self.model.operate(Buttons_Enum.CLEAR.value) == None
        self.view.clear_panel()