import random
import tkinter
from i_controller import i_controller

class View:
    def __init__(self, i_controller): 
        self.i_controller = i_controller
        self.app_window = tkinter.Tk()
        self.app_window.title("crazy calculator")
        self.panel = tkinter.Text(self.app_window, height=2, width=30)
        self.panel.pack()
        self.digits_frame = tkinter.Frame(self.app_window)
        self.digits_frame.pack()
        self.__create_buttons()

    def show_input_on_panel(self, some_text):
        self.panel.insert(tkinter.END, some_text)

    def show_output_on_panel(self, some_text):
        self.panel.insert(tkinter.END, some_text)

    def show_calculator(self):
        self.app_window.mainloop()

    def __create_buttons(self):
        for i in range(10):
            B = tkinter.Button(self.digits_frame, text = i, command = lambda i=i: self.show_input_on_panel(i), height=1, width=4)
            B.grid(row=(i//3),  column=i%3)
