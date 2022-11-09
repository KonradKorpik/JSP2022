i = int(input("Podaj i:"))

print('\n')

for x in range(1, i+1):
     for y in range(1, 11):
         print (y*x, end="\t")
     print()
