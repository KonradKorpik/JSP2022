def szyfr(tekst, wyb):
    if wyb == 1:
        klucz={
            "a" : "y",
            "e" : "i",
            "i" : "o",
            "o" : "a",
            "y" : "e"
        }
        lista = list(tekst)

        for z in range(0, len(tekst), 1):
            for x, y in klucz.items():
                if tekst[z] == x:
                    lista[z] = y
        return "".join(lista)
    elif wyb == 2:
        klucz={
            "y": "a",
            "i": "e",
            "o": "i",
            "a": "o",
            "e": "y"
        }
        lista = list(tekst)
        
        for z in range(0, len(tekst), 1):
            for x, y in klucz.items():
                if tekst[z] == x:
                    lista[z] = y
        return "".join(lista)

print(szyfr("ta jist maj tiskt", 2))
