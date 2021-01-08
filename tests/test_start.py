import unittest
import sys 
sys.path.append('/home/adi/Calculator/src')

from state import State
from start import Start
from model import Model
from state_factory import State_factory

class test_start(unittest.TestCase):
    def test_fresh_start_get_next_state_name(self):
        model = Model()
        factory = State_factory()
        start1 = Start(factory, model)
        start1.operate("C")
        self.assertEqual(start1.get_next_state_name(), "Start")
        start1.operate("=")
        self.assertEqual(start1.get_next_state_name(), "Start")
        start1.operate("/")
        self.assertEqual(start1.get_next_state_name(), "Error")
        start1.operate("x")
        self.assertEqual(start1.get_next_state_name(), "Error")
        start1.operate("+")
        self.assertEqual(start1.get_next_state_name(), "Error")
        start1.operate("-")
        self.assertEqual(start1.get_next_state_name(), "Storing_digits_for_first_operand")
        start1.operate("8")
        self.assertEqual(start1.get_next_state_name(), "Storing_digits_for_first_operand")

if __name__ == "__main__":
    ts1 = test_start()
    ts1.test_fresh_start_get_next_state_name()





    