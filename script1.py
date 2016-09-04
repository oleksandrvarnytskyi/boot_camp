class Selfness:
    def selfness(self, a1, a2):
        return a1 + a2


obj = Selfness()
t = Selfness.selfness
print t(obj, 2, 3)
