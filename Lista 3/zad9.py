from time import process_time_ns


m = int(input("Podaj m: "))
n = int(input("Podaj n: "))
tablicaa = []
tablicab = []

for x in range(1, m + 1):
    for y in range(1, n + 1):
        tablicab.append(x * y)
    tablicaa.append(tablicab)
    tablicab = []
print(tablicaa)
