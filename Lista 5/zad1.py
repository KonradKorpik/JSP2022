def zamiana(liczba):
    wynik = 0
    liczby = {
        "dziesciec": 10,
        "dwadziescia": 20,
        "trzydziesci": 30,
        "czterdziesci": 40,
        "piecdziesiat": 50,

        "jedenascie": 11,
        "dwanascie": 12,
        "trzynascie": 13,
        "czternascie": 14,
        "pietnascie": 15,
        "szesnascie": 16,
        "siedemnascie": 17,
        "osiemnascie": 18,
        "dziewietnascie": 19,

        "jeden": 1,
        "dwa": 2,
        "trzy": 3,
        "cztery": 4,
        "piec": 5,
        "szesc": 6,
        "siedem": 7,
        "osiem": 8,
        "dziewiec": 9,
    }
    
    if " " in liczba:
        lista = list(liczba)
        i = lista.index(" ")
        dziesiatek = "".join(lista[:i])
        jednosci = "".join(lista[i + 1:])
        wynik = liczby[dziesiatek] + liczby[jednosci]
    else:
        wynik = liczby[liczba]
    return wynik
    
licz = input("Podaj liczbe slownie: ")
print(zamiana(licz))
