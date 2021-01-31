import unittest

from src.state_factory import State_factory
from src.model import Model
from src.start import Start
from src.error import Error
# from expression import Expression

class Test_factory(unittest.TestCase):
    mdl = Model()
    factory = State_factory(mdl)
   
    def test_create_state(self):
        state = self.factory.create_state()
        self.assertIsInstance(state, Start)
    
    # def test_create_from(self):
    #    start = Start(factory, mdl, )

if __name__ == "__main__":
    tst = Test_factory()
    tst.test_create_state()