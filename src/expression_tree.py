from abc import ABC, abstractmethod
from src.common import Buttons_Enum as Btns

class Component(ABC):
    @abstractmethod
    def __init__(self, item):
        self.value = item

      
    @abstractmethod
    def operate(self):
        pass

    def get_value(self):
        return self.value

    @abstractmethod
    def print_component(self):
        pass


class Operand(Component):
    def __init__(self, item):
        Component.__init__(self,item)
    
    def operate(self):
        return self.value
    
    def print_component(self):
        print(self.value)
    

class Operator(Component):
    @abstractmethod
    def __init__(self, item):
        Component.__init__(self,item)
        self.left = None
        self.right = None

    def add_child(self, component):
        if self.right == None:
            self.right = component
        else:
            assert self.left == None
            self.left = component

    def print_component(self):
        self.left.print_component()
        self.right.print_component()
        print(self.value)


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

    #may throw ZeroDivisionError exception
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
    

class Expression_tree:
    def __init__(self):
        self.tree = []
    
    def build_tree(self, postfix_component_list):
        for i in postfix_component_list:
            if isinstance(i, Operator):
                assert len(self.tree) > 1
                i.add_child(self.tree.pop())
                i.add_child(self.tree.pop())
            self.tree.append(i)

    def evaluate(self):
        print(len(self.tree))
        assert len(self.tree) == 1
        return self.tree[0].operate()

    def print_postorder(self):
        self.tree[0].print_component()
    
    def clear_tree(self): 
        self.tree.clear()  
    