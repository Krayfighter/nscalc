import gmpy2
from gmpy2 import mpfr, mpq

gmpy2.get_context().precision=200



# wrapper class for gmpy2.gmpy2.mpq type
# with geometric operations
class mpratio:
    def __init__(self, x, y):
        self.data = mpq(x, y)
    
    # rotates a point around the origin
    # WARNING only supports multiples of 90 
    def rotate(self, degree: int):
        if degree == 90 or -270:
            self.data = mpq(
                self.data.numerator,
                self.data.denominator*-1
            )
        elif degree == 180 or -180:
            self.mpratio_rotate(90)
            self.mpratio_rotate(90)
        elif degree == 270 or -90:
            self.mpratio_rotate(180)
            self.mpratio_rotate(90)
        elif degree == 360 or 0 or -360:
            pass
        else:
            print("Invalid degree value")
    
    def __str__(self):
        return str(self.data.denominator)+"/"+str(self.data.numerator)



# wrapper class for the gmpy2.gmpy2.mpfr type
class mpnum:
    def __init__(self, x, e: int = 0):
        if type(x) == str:
            self.data = mpfr(x)*10**e
        elif type(x) == mpfr:
            self.data = x
    
    def __add__(self, other):
        self.data += other.data
        return mpnum(self.data)
    
    def __sub__(self, other):
        self.data -= other.data
        return mpnum(self.data)
    
    def __mul__(self, other):
        self.data *= other.data
        return mpnum(self.data)
    
    def __div__(self, other):
        self.data /= other.data
        return mpnum(self.data)
    
    def __truediv__(self, other):
        self.data /= other.data
        return mpnum(self.data)

    def __str__(self):
        e = 0
        number = self.data
        if number == 0:
            return str(0)
        if number > 0:
            while True:
                print(number)
                if number>=10:
                    number /= 10
                    e += 1
                else:
                    break
        else:
            while True:
                if number <= 10:
                    number *= 10
                    e -= 1
                else:
                    break
        
        return str(number)+"e+"+str(e)
    
    def pow(self, e):
        self.data = pow(self.data, e)
        return mpnum(self.data)
