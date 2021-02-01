from src.i_controller import i_controller
from src.view import View
from src.model import Model
from src.buttons_enum import Buttons_Enum

class Controller(i_controller):
    def __init__(self):
        self.model = Model()
        self.view = View(self)
        self.result_was_shown = False

    def start(self):
        self.view.show_calculator()

    def add_digit(self, digit):
        if self.result_was_shown:
            self.view.clear_panel()
            self.result_was_shown = False
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
            self.result_was_shown = True


    def restart(self):
        assert self.model.restart() == None
        self.view.clear_panel()