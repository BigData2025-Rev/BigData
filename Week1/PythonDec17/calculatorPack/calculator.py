from abc import ABC, abstractmethod
class Calculator(ABC):
    
    @abstractmethod
    def addition(self, num1, num2):
        pass

    @abstractmethod
    def subtraction(self, num1, num2):
        pass

    @abstractmethod
    def rounding(self, result):
        pass
    