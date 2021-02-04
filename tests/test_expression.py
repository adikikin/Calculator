import unittest

from src.expression import Expression
from src.buttons_enum import Buttons_Enum as ops

class Test_exp(unittest.TestCase):
    def test_exp_scenario(self):
        exp = Expression()
        exp.add_digit_to_first_operand(4)
        # exp.add_digit_to_first_operand(8)
        # exp.add_digit_to_first_operand(1)
        self.assertEqual(exp.first_operand, 4)
        exp.add_operator(ops.MUL.value)
        self.assertEqual(exp.operator, ops.MUL.value)
        exp.add_digit_to_second_operand(5)
        self.assertEqual(exp.second_operand, 5)
        exp.add_operator(ops.ADD.value)
        self.assertEqual(exp.first_operand, 20)
        exp.add_digit_to_second_operand(6)
        self.assertEqual(exp.second_operand, 6)


if __name__ == "__main__":
    unittest.main()