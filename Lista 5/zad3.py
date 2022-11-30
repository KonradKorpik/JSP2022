def zamiana(rzymska):
    klucze = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    liczba = 0
    ostatnia = 0

    for z in range(len(rzymska), 0, -1):
       for x, y in klucze.items():
            if rzymska[z - 1] == x:
                if y >= ostatnia:
                    ostatnia = y
                    liczba += y
                else:
                    liczba -= y
    return liczba
            
rzmska = input("Podaj liczbe rzymska: ")
print(zamiana(rzmska))
