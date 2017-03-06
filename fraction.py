from support import gcd
class Fraction:
    def __init__(self,num,den):
        g = gcd(num,den)
        self.num = num//g
        self.den = den//g
    def inverse(self):
        return Fraction(self.den, self.num)

    def reduce(self):
        g = gcd(self.num,self.den)
        self.num //= g
        self.den //= g

    def __eq__(self,other):
        self.reduce()
        other.reduce()
        return (self.num,self.den) == (other.num,other.den)
    def __ge__(self,other):
        return self.num*other.den > self.den*other.num

    def __add__(self,other):
        if type(other) == type(0):
            return Fraction(self.num + other*self.den, self.den)

        return Fraction(self.num*other.den + other.num*self.den,
                        self.den*other.den)
    def __sub__(self,other):
        if type(other) == type(0):
            return Fraction(self.num - other*self.den, self.den)

        return Fraction(self.num*other.den - other.num*self.den,
                        self.den*other.den)
    def __mul__(self,other):
        if type(other) == type(0):
            return Fraction(self.num*other, self.den)

        return Fraction(self.num*other.num, self.den*other.den)
    def __str__(self):
        return str(int(self.num))+"/"+str(int(self.den))
