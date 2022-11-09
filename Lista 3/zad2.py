liczba = int(input())

if (liczba%2==0):
    print("parzysta")
else:
    print("nieparzysta")

typ = ['parzysta', 'nieparzysta']
print(typ[liczba%2])
