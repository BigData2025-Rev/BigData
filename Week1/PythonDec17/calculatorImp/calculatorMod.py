from calculatorPack.calculator import Calculator
from calculatorImp.funexcept import CustomException
import numbers


class CalculatorImp(Calculator):
    def addition(self, num1: int, num2: int)-> int:
        if isinstance(num1,numbers.Number) and isinstance(num2, numbers.Number): #check to make sure input is numeric
            result = num1 + num2
            return result
        else:
            raise CustomException("One or more entries were not numeric")
    
    def subtraction(self, num1: int, num2: int)-> int:
        if isinstance(num1,numbers.Number) and isinstance(num2, numbers.Number): #check to make sure input is numeric
            result = num1 - num2
            return result
        else:
            raise CustomException("One or more entries were not numeric")
        
    def rounding(self, result: float) -> int:
        if isinstance(result, numbers.Number): #check to make sure input is numeric
            return round(result)
        else:
            raise CustomException("Could not round the value")

calc = CalculatorImp()
print(calc.addition(5,5))