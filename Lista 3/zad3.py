import math

a=0
while (a==0):
    a = int(input())
b = int(input())
c = int(input())

delta = b**2-4*a*c
if (delta>0):
    x1=((-b)+math.sqrt(delta))/(2*a)
    x2=((-b)-math.sqrt(delta))/(2*a)

    print(x1)
    print(x2)
elif (delta==0):
    x=(-b)/(2*a)

    print(x)
else:
    print("brak")
