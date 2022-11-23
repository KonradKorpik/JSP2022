import math

def f(n, switch="d2r"):
    if switch == "r2d":
        degres = n * (180 / math.pi)
        print(degres)
    else:
        radians = n * (math.pi / 180)
        print(radians)

f(90, "r2d")
