def f(tablica):
    niepowtorzone = []
    for x in range(0, len(tablica)):
        if tablica[x] in niepowtorzone:
            tablica[x] = []
        else:
            niepowtorzone.append(tablica[x])
    print(niepowtorzone)

f([1, 2, 1, 2, 3, 4, 3, 4])
