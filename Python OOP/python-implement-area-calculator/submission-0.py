import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, *args) -> float:
        if len(args) == 1:
            return math.pi * args[0] * args[0]
        else:
            result = 1.0
            for arg in args:
                result *= arg
            return result
        

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
