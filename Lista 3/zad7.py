n = int(input("Podaj ilosc liczb? "))

n1, n2 = 0, 1
count = 0

if n <= 0:
   print("Podaj liczbe!")
elif n == 1:
   print(n," liczb:")
   print(n1)
else:
   print("Liczby Fibonacci:")
   while count < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
