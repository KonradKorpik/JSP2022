import random
import time
import zad2

def bombelki(zbior):
    for i in range(0, len(zbior) - 1):
        for j in range(0, len(zbior) - 1):
            if zbior[j + 1] < zbior[j]:
                zbior[j + 1], zbior[j] = zbior[j], zbior[j + 1]
    return zbior


t1 = time.time()
zbior = []
for i in range(100, 400, 100):
    for j in range(0, i):
        i = random.randint(0, 20)
        zbior.append(i)
    t2 = time.time()
    print(bombelki(zbior))
    print("bombelkowy czas= ", t2 - t1)

print(zad2)
