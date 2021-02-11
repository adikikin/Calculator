from abc import ABC, abstractmethod
from buttons_enum import Buttons_Enum as Btns

class Component(ABC):
    @abstractmethod
    def __init__(self, item):
        self.value = item
    
    @abstractmethod
    def operate(self):
        pass


class Operand(Component):
    def __init__(self, item):
        Component.__init__(self,item)
    
    def operate(self):
        return self.value
    

class Operator(Component):
    @abstractmethod
    def __init__(self, item):
        Component.__init__(self,item)
        self.left = None
        self.right = None
  

    def add_child(self, component):
        if self.left == None:
            self.left = component
        else:
            assert self.right == None
            self.right = component


class Add(Operator):
    def __init__(self, item):
        Operator.__init__(self,item)

    def operate(self):
        assert self.left != None and self.right != None
        return self.left.operate() + self.right.operate()


class Sub(Operator):
    def __init__(self, item):
        Operator.__init__(self,item)

    def operate(self):
        assert self.left != None and self.right != None
        return self.left.operate() - self.right.operate()


class Mul(Operator):
    def __init__(self, item):
        Operator.__init__(self,item)

    def operate(self):
        assert self.left != None and self.right != None
        return self.left.operate() * self.right.operate()
    

class Div(Operator):
    def __init__(self, item):
        Operator.__init__(self,item)

    def operate(self):
        assert self.left != None and self.right != None
        return self.left.operate() / self.right.operate()


class Component_Factory:
    def __init__(self):
        self.ops = {
                    Btns.ADD.value : Add,
                    Btns.SUB.value : Sub,
                    Btns.MUL.value : Mul,
                    Btns.DIV.value : Div,
                    }

    def Create_component(self, item):
        if item in self.ops:
            return self.ops[item](item)
        else:
            assert type(item) == int or type(item) == float
            return Operand(item)
    