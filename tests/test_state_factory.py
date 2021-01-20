import unittest
import sys
sys.path.append('/home/adi/Calculator/src')

from state_factory import State_factory
from model import Model
from start import Start
from error import Error


class Test_factory(unittest.TestCase):
    mdl = Model()
    factory = State_factory(mdl)
   
    def test_create_state(self):
        state = self.factory.create_state()
        self.assertIsInstance(state, Start)
    
    # def test_create_from(self):
       

if __name__ == "__main__":
    tst = Test_factory()
    tst.test_create_state()