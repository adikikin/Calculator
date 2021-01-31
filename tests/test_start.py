import unittest

from src.state import State
from src.start import Start
from src.model import Model
from src.state_factory import State_factory
from src.states_enum import States_enum
from src.expression import Expression
from src.storing_digits_for_first_operand import Storing_digits_for_first_operand
from src.error import Error
from src.buttons_enum import Buttons_Enum as Btns

class test_start(unittest.TestCase):
    def test_add_digit(self):
        model = Model()       
        factory = State_factory(model)
        exp = Expression()
        start1 = Start(factory,model, exp)
        result = start1.add_digit("4")
        # self.assertEqual(start1.get_next_state_enum(), States_enum.STORING_DIGITS_FOR_FIRST_OPERAND)
        self.assertEqual(result, "4")
        self.assertIsInstance(model.state, Storing_digits_for_first_operand)
    
    def __test_operator(self, operator):
        model = Model()       
        factory = State_factory(model)
        exp2 = Expression()
        strt = Start(factory, model, exp2)
        result = strt.add_operator(operator)
        # self.assertEqual(strt.get_next_state_enum(), States_enum.ERROR)
        self.assertEqual(result, States_enum.ERROR.name)
        self.assertIsInstance(model.state, Error)

    def test_mul_add_div(self):
        for op in [Btns.MUL.value, Btns.ADD.value, Btns.DIV.value]:
            self.__test_operator(op)
    
    def test_sub(self):
        model = Model()       
        factory = State_factory(model)
        exp2 = Expression()
        strt = Start(factory, model, exp2)
        result = strt.add_operator(Btns.SUB.value)
        # self.assertEqual(strt.get_next_state_enum(), States_enum.STORING_DIGITS_FOR_FIRST_OPERAND)
        self.assertEqual(result, Btns.SUB.value)
        self.assertIsInstance(model.state, Storing_digits_for_first_operand)
        self.assertEqual(exp2.sign, -1)


if __name__ == "__main__":
    ts1 = test_start()
    ts1.test_add_digit()
    ts1.test_mul_add_div()
    ts1.test_sub()




    