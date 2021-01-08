import unittest
import sys 
sys.path.append('/home/adi/Calculator/src')

from model import Model

class Test_model(unittest.TestCase):
    def test_return_val_in_start_state(self):
        model1 = Model()
        self.assertIsNone(model1.operate("C"))
        self.assertIsNone(model1.operate("="))
        self.assertEqual(model1.operate("/"), "Error")
        self.assertEqual(model1.operate("x"), "Error")
        self.assertEqual(model1.operate("+"), "Error")
        self.assertEqual(model1.operate("-"), "-")
        self.assertEqual(model1.operate("8"), "8")





if __name__ == "__main__":
    tst = Test_model()
    tst.test_return_val_in_start_state()
    