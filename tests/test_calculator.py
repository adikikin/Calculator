import sys
sys.path.append('/home/adi/Calculator/src')

from view import View
from controller import Controller

if __name__ == "__main__":
    ctrl = Controller()
    ctrl.start()