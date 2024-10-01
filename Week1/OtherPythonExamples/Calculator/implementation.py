import CalculatorInterface.interface as ifc
import numbers

class CustomException (Exception):
    def __init__(self,message):
        self.message = message

class CalculatorImp(ifc.Calculator):
    def addition(self, num1: int, num2:int ) -> int:
        if isinstance(num1,numbers.Number) and isinstance(num2,numbers.Number):
            result = num1+num2
            return result
        else:
            raise CustomException("One or more entries were not numeric")
        
    def subtraction(self, num1: int, num2:int ) -> int:
        if isinstance(num1,numbers.Number) and isinstance(num2,numbers.Number):
            result = num1 - num2
            return result
        else:
            raise CustomException("One or more entries were not numeric")
        
    def rounding(self, result: float) -> int:
        if isinstance(result, numbers.Number):
            return round(result)
        else:
            raise CustomException("Could not round the value")
