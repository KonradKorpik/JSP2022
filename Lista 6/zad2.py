import SzyfrCezara as sc

tekst = input("Podaj tekst do zaszyfrowania: ")
print("Zaszyfrowany tekst: ", sc.szyfruj(tekst, 1))
tekst2 = input("Podaj teskt do odszyfrowania: ")
print("Odszyfrowany tekst: ", sc.odszyfruj(tekst2, 1))
