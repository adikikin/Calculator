from abc import ABC, abstractmethod

class i_controller(ABC):
    @abstractmethod
    def add_digit(self, digit):
        pass

    @abstractmethod
    def add_operator(self, operator):
        pass

    @abstractmethod
    def evaluate(self):
        pass

    @abstractmethod
    def restart(self):
        pass

