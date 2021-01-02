import random
import tkinter

class View:
    def __init__(self):  #TODO add i_controller as argument
        #self.i_controller = i_controller
        self.app_window = tkinter.Tk()
        self.app_window.title("crazy calculator")
        self.panel = tkinter.Text(self.app_window, height=2, width=30)
        self.panel.pack()
        self.__create_buttons()

    def show_on_panel(self, some_text):
        self.panel.insert(tkinter.END, some_text)

    def show_calculator(self):
        self.app_window.mainloop()

    def __create_buttons(self):
        for i in range(10):
            B = tkinter.Button(self.app_window, text = i, command = lambda i=i: self.show_on_panel(i))
            B.pack()


# if __name__ == "__main__":
#     view1 = View()
#     view1.show_calculator()

