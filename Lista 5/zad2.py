def zamiana(liczba):
    tysiecy = {
        1: "tysiac",
    }
    setek = {
        1: "sto",
        2: "dwiescie",
        3: "trzysta",
        4: "czterysta",
        5: "piecset",
        6: "szescset",
        7: "siedemset",
        8: "osiemset",
        9: "dziewiecset",
    }
    dziesiatek = {
        1: "dziesiec",
        2: "dwadziescia",
        3: "trzydziesci",
        4: "czterdziesci",
        5: "piecdziesiat",
        6: "szescdziesiat",
        7: "siedemdziesiat",
        8: "osiemdziesiat",
        9: "dziewiecdziesiat"
    }
    jednosci = {
        1: "jeden",
        2: "dwa",
        3: "trzy",
        4: "cztery",
        5: "piec",
        6: "szesc",
        7: "siedem",
        8: "osiem",
        9: "dziewiec",
    }

    strLiczba = str(liczba)
    wynik = ""
    if len(strLiczba) == 1:
        for x, y in jednosci.items():
            if int(strLiczba[0]) == x:
                wynik = y

    if len(strLiczba) == 2:
            for x, y in dziesiatek.items():
                if int(strLiczba[0]) == x:
                    wynik = y
            for x, y in jednosci.items():
                if int(strLiczba[1]) == x:
                    wynik = wynik + " " + y

    if len(strLiczba) == 3:
        for x, y in setek.items():
            if int(strLiczba[0]) == x:
                wynik = y
        for x, y in dziesiatek.items():
            if int(strLiczba[1]) == x:
                wynik = wynik + " " + y
        for x, y in jednosci.items():
            if int(strLiczba[2]) == x:
                wynik = wynik + " " + y

    if len(strLiczba) == 4:
        for x, y in tysiecy.items():
            if int(strLiczba[0]) == x:
                wynik = y
        for x, y in setek.items():
            if int(strLiczba[1]) == x:
                wynik = wynik + " " + y
        for x, y in dziesiatek.items():
            if int(strLiczba[2]) == x:
                wynik = wynik + " " + y
        for x, y in jednosci.items():
            if int(strLiczba[3]) == x:
                wynik = wynik + " " + y
    return wynik

number = int(input("Podaj liczbe do zamiany: "))
print(zamiana(number))
