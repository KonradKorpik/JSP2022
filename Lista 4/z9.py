import math

def silniaBiblio(x):
    x = abs(int(x))
    return math.factorial(x)

def silnia(x):
    x = abs(int(x))
    i = 1
    for z in range(1,x+1):
        i*=z
    return i
print(silnia(-5.231))