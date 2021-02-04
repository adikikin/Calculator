import unittest
# import sys 
# sys.path.append('/home/adi/Calculator/src')

from src.state import State
from src.start import Start
from src.model import Model
from src.state_factory import State_factory
from src.states_enum import States_enum
from src.expression import Expression
from src.storing_digits_for_first_operand import Storing_digits_for_first_operand
from src.stored_operand import Stored_operand
from src.stored_operator import Stored_operator
from src.buttons_enum import Buttons_Enum as Btns

class test_stored_operand(unittest.TestCase):
    def test_add_digit(self):
        model = Model()       
        factory = State_factory(model)
        exp = Expression()
        model.state.expression.first_operand = "8"
        start1 = Stored_operand(factory,model, exp)
        result = start1.add_digit("4")
        self.assertEqual(result, "4")
        self.assertIsInstance(model.state, Storing_digits_for_first_operand)
        self.assertEqual(model.state.expression.first_operand, "4")

    def __test_operator(self, operator):
        model = Model()       
        factory = State_factory(model)
        exp2 = Expression()
        strt = Stored_operand(factory, model, exp2)
        result = strt.add_operator(operator)
        self.assertEqual(result, operator)
        self.assertIsInstance(model.state, Stored_operator)
        self.assertEqual(model.state.expression.operator, operator)

    def test_mul_add_div_sub(self):
        for op in [Btns.MUL.value, Btns.ADD.value, Btns.DIV.value, Btns.SUB.value]:
            self.__test_operator(op)
    
    def test_start(self):
        model = Model()       
        factory = State_factory(model)
        exp2 = Expression()
        model.state.expression.first_operand = "8"
        strt = Stored_operand(factory, model, exp2)
        model.state = strt
        result = strt.restart()
        self.assertEqual(result, None)
        self.assertIsInstance(model.state, Start)
        self.assertEqual(model.state.expression.first_operand, 0)


    def test_equal(self):
        model = Model()       
        factory = State_factory(model)
        exp2 = Expression()
        model.state.expression.first_operand = "8"
        strt = Stored_operand(factory, model, exp2)
        model.state = strt
        result = strt.evaluate()
        self.assertEqual(result, model.state.expression.get_first_operand())
        self.assertIsInstance(model.state, Stored_operand)



if __name__ == "__main__":
    ts1 = test_stored_operand()
    ts1.test_add_digit()
    ts1.test_mul_add_div_sub()
    ts1.test_start()
    ts1.test_equal()




    