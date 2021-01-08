from abc import ABC, abstractmethod

class I_model:
    @abstractmethod
    def change_state(self, state):
        pass