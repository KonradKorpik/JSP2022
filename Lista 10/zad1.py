import math

class Kolo():
    def __init__(self, r):
        self.r = r
    def area(self):
        return self.r**2 * math.pi
    def obw(self):
        return 2 * self.r * math.pi

Kolo1 = Kolo(10)

print("Pole: ", Kolo1.area(), " Obwód: ", Kolo1.obw())
