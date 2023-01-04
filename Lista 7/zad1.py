import datetime

def fibonacci1(n):
    i = 0
    n1, n2 = 0, 1

    if n == 1:
        print(n1)
    else:
        while i < n:
            print(n1)
            suma = n1 + n2
            n1 = n2
            n2 = suma
            i += 1
def fibonacci2(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci2(n - 1) + fibonacci2(n - 2)

n = int(input("Podaj n: "))
start = datetime.datetime.now()
fibonacci1(n)
duration = datetime.datetime.now() - start
print(duration)
n = int(input("Podaj n: "))
start = datetime.datetime.now()
print(fibonacci2(n))
duration = datetime.datetime.now() - start
print(duration)
