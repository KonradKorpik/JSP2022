import datetime
import random

def sortowaniePrzezWstawianie(lista, n):
    for x in range(1, n):
        teraz = lista[x]
        y = x - 1
        while y >= 0 and teraz < lista[y]:
            lista[y + 1] = lista[y]
            y -= 1
        lista[y + 1] = teraz
    print(lista)

lista100 = []
lista200 = []
lista300 = []

for i in range(100):
    lista100.append(random.randint(0, 20)) 
for i in range(200):
    lista200.append(random.randint(0, 20)) 
for i in range(300):
    lista300.append(random.randint(0, 20)) 

start = datetime.datetime.now()
sortowaniePrzezWstawianie(lista100, 100)
duration = datetime.datetime.now() - start
print(duration)
start = datetime.datetime.now()
sortowaniePrzezWstawianie(lista200, 200)
duration = datetime.datetime.now() - start
print(duration)
start = datetime.datetime.now()
sortowaniePrzezWstawianie(lista300, 300)
duration = datetime.datetime.now() - start
print(duration)
