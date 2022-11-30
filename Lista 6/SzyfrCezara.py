def szyfruj(tekst, klucz):
    zaszyfrowany = ""
    for i in range(len(tekst)):
        if ord(tekst[i]) >= 65 and ord(tekst[i]) <= 90:
            if ord(tekst[i]) + klucz > 90:
                zaszyfrowany += chr(ord(tekst[i]) + klucz - 26)
            else:
                zaszyfrowany += chr(ord(tekst[i]) + klucz)
        elif ord(tekst[i]) >= 97 and ord(tekst[i]) <= 122:
            if ord(tekst[i]) + klucz > 122:
                zaszyfrowany += chr(ord(tekst[i]) + klucz - 26)
            else:
                zaszyfrowany += chr(ord(tekst[i]) + klucz)
        else:
            zaszyfrowany += tekst[i]
    return zaszyfrowany
def odszyfruj(tekst, klucz):
    odszyfrowany = ""
    for i in range(len(tekst)):
        if ord(tekst[i]) >= 65 and ord(tekst[i]) <= 90:
            if ord(tekst[i]) - klucz < 65:
                odszyfrowany += chr(ord(tekst[i]) - klucz + 26)
            else:
                odszyfrowany += chr(ord(tekst[i]) - klucz)
        elif ord(tekst[i]) >= 97 and ord(tekst[i]) <= 122:
            if ord(tekst[i]) - klucz < 97:
                odszyfrowany += chr(ord(tekst[i]) - klucz + 26)
            else:
                odszyfrowany += chr(ord(tekst[i]) - klucz)
        else:
            odszyfrowany += tekst[i]
    return odszyfrowany
