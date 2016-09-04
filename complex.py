import math


class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return Complex(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        return Complex(self.re*other.re - self.im*other.im, self.re*other.im +
                       self.im*other.re)

    def __eq__(self, other):
        return self.re == other.re and self.im == other.im

    def __ne__(self, other):
        return self.re != other.re and self.im != other.im

    def complex_abs(self):
        return math.hypot(self.re, self.im)

    def __str__(self):
        if self.im < 0:
            return '%d%di' % (self.re, self.im)
        else:
            return '%d+%di' % (self.re, self.im)


a = Complex(2, 3)
b = Complex(4, -7)
z = Complex()

print a
print b
print z
print '-' * 33
c = a + b
print c
print '-' * 33
d = a * b
print d
print '-' * 33
print a.complex_abs()
