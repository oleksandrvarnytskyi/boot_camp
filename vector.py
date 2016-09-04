import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def vector_len(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)


a = Vector(2, 3)
b = Vector(4, 7)
z = Vector()

print 'a: ', a
print 'b: ', b
print 'z: ', z
print a == b
print a != z
print '-' * 33
a += b
print a
print '-' * 33
b -= a
print b
print '-' * 33
c = a + b
print c
print '-' * 33
print 'Vector length: %.3f' % a.vector_len()
