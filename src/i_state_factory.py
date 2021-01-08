from abc import ABC, abstractmethod

class I_state_factory:
    @abstractmethod
    def create_state_from(self, state):
        pass