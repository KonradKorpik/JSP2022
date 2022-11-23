string = input("Podaj elementy tablicy, po spacji: ")
tablica = string.split()
for x in range(0, len(tablica)):
    tablica[x] = int(tablica[x])
dzialanie = int(input("Wybierz dzialanie (0 - dodawanie, 1 - mnozenie): "))

if dzialanie == 0:
    suma = tablica[0]
    for x in range(1, len(tablica)):
        suma += tablica[x]
    print(suma)
if dzialanie == 1:
    iloczyn = tablica[0]
    for x in range(1, len(tablica)):
        iloczyn *= tablica[x]
    print(iloczyn)
