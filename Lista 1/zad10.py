import cmath

z = 1j
x = cmath.sin(z)
y = cmath.cos(z)

print("Wartosc rzeczywista i urojona sin(z): ")
print(x.real, x.imag, sep=" ; ")
print("Wartosc rzeczywista i urojona cos(z): ")
print(y.real, y.imag,"\n", sep=" ; ")
print(x**2+y**2)
#Funkcje zdefiniowane w "cmath" zawsze zwracają liczbę zespoloną
