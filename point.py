import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y

    def distance(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

if __name__ == '__main__':
    a = Point(2, 3)
    b = Point(4, 7)
    z = Point()

    print 'a: ', a
    print 'b: ', b
    print 'z: ', z
    print a == b
    print a != z
    print 'Distance: ', a.distance(b)

    a.x = 8
    print a
