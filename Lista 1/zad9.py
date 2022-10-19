import cmath

z = complex(input())

print("Modul: ", abs(z))
print("Argument: ", cmath.phase(z))
print(z.conjugate())
