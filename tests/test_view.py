import sys

from src.view import View

class i_controller:
    pass

if __name__ == "__main__":
    i_ctrl_mock = i_controller()
    view1 = View(i_ctrl_mock)
    view1.show_calculator()

