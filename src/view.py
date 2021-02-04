import random
import copy
from tkinter import Tk, Text, Frame, LEFT, RIGHT, END, Button
from src.i_controller import i_controller
from src.buttons_enum import Buttons_Enum

class View:
    def __init__(self, i_controller): 
        self.i_controller = i_controller
        self.app_window = Tk()
        self.app_window.title("crazy calculator")
        self.panel = Text(self.app_window, height=2, width=30)
        self.panel.bind("<Key>", lambda e: "break")
        self.panel.pack() 
        self.__create_digit_buttons()
        self.__create_operator_buttons()

    def show_on_panel(self, some_text):
        self.panel.insert(END, some_text)

    def show_calculator(self):
        self.app_window.mainloop()

    def clear_panel(self):
        self.panel.delete('1.0', END)

    def __receive_input(self, usr_input):
        if usr_input in range(10):
            self.i_controller.add_digit(usr_input)
        elif usr_input == Buttons_Enum.CLEAR.value:
            self.i_controller.restart()
        elif usr_input == Buttons_Enum.EQUAL.value:
            self.i_controller.evaluate()
        else:
            self.i_controller.add_operator(usr_input)

    def __create_buttons(self, buttons_list, frame, num_of_columns):
        for i, item in enumerate(buttons_list):
            button = Button(frame, text = item, command = lambda item=item: self.__receive_input(item), height=1, width=4)
            button.grid(row=(i//num_of_columns), column=i%num_of_columns)


    def __create_digit_buttons(self):
        self.digits_frame = Frame(self.app_window)
        self.digits_frame.pack(side=LEFT,  padx=10, pady=10)
        self.__create_buttons(range(10), self.digits_frame, 3)


    def __create_operator_buttons(self):
        self.operators_frame = Frame(self.app_window)
        self.operators_frame.pack(side=RIGHT, padx=10)
        buttons_list = [member.value for member in Buttons_Enum]
        self.__create_buttons(buttons_list, self.operators_frame, 2)
