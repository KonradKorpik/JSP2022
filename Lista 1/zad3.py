import math

a = int(input("Podaj bok a: "))
b = int(input("Podaj bok b: "))
kat = int(input("Podaj kat: "))
pole = 1/2*(a*b)*math.sin(kat*math.pi/180)

print("Pole: ", round(pole,4))
