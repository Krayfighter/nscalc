from sympy import Float, sqrt

class Equation():
    def __init__(self, input, mode = "Float"):
        self.input = input
        self.mode = mode
    
    def parse(self):
        pass
    
    class eobj():
        def __init__(self, obj_type: str, value):
            self.otype = obj_type
            self.value = value
        
        def append(self, value):
            self.value += value
        
        def format(self):
            if self.otype == "num":
                self.value = self.mode + "(" + self.value + ")"


def invsqrt(number: str):
    return 1/sqrt(Float(number))

def enotation(number: str):
    return Float(number)