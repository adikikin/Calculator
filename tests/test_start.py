import unittest
import sys 
sys.path.append('/home/adi/Calculator/src')

from state import State
from start import Start
from model import Model
from state_factory import State_factory
from states_enum import States_enum


class test_start(unittest.TestCase):
    def test_fresh_start_get_next_state_name(self):
        model = Model()
        factory = State_factory(model)
        start1 = Start(factory, model)
        start1.operate("C")
        self.assertEqual(start1.get_next_state_name(), States_enum.START)
        start1.operate("=")
        self.assertEqual(start1.get_next_state_name(), States_enum.START)
        start1.operate("/")
        self.assertEqual(start1.get_next_state_name(), States_enum.ERROR)
        start1.operate("x")
        self.assertEqual(start1.get_next_state_name(), States_enum.ERROR)
        start1.operate("+")
        self.assertEqual(start1.get_next_state_name(), States_enum.ERROR)
        start1.operate("-")
        self.assertEqual(start1.get_next_state_name(), States_enum.STORING_DIGITS_FOR_FIRST_OPERAND)
        start1.operate("8")
        self.assertEqual(start1.get_next_state_name(), States_enum.STORING_DIGITS_FOR_FIRST_OPERAND)


    def test_return_val(self):
        model = Model()
        factory = State_factory(model)
        start1 = Start(factory, model)
        self.assertEqual(start1.operate("8"), "8")
        self.assertEqual(start1.operate("-"), "-")
        self.assertEqual(start1.operate("C"), None)
        self.assertEqual(start1.operate("x"), "ERROR")
        self.assertEqual(start1.operate("="), None)
        self.assertEqual(start1.operate("/"), "ERROR")
        self.assertEqual(start1.operate("+"), "ERROR")







if __name__ == "__main__":
    ts1 = test_start()
    ts1.test_fresh_start_get_next_state_name()
    ts1.test_return_val()




    