def lookAndSay(liczba):
    wynik = ""
    powtorz = liczba[0]
    liczba = liczba[1:] + " "
    ile = 1

    for teraz in liczba:
        if teraz != powtorz:
            wynik += str(ile) + powtorz
            ile = 1
            powtorz = teraz
        else:
            ile += 1
    return wynik

liczba = "1"
n = int(input("Podaj n: "))
for i in range(n):
    print(liczba)
    liczba = lookAndSay(liczba)
