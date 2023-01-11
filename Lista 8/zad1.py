import os.path
import time
from datetime import date
import cezar

today = date.today()
year = str(today.year)
month = str(today.month)
day = str(today.day)
key = 11

while (key > 10) or (key < 1):
    key = int(input("Podaj przesunięcie szyfru (od 1 do 10): "))

strKey = str(key)
name = input("Podaj nazwe pliku do zaszyfrowania: ");
name = name + ".txt"
path = input("Podaj ścieżkę zapisu pliku: ");
namefile = "plik_zaszyfrowany" + strKey + '_' + str(today.year) + str(today.month) + str(today.day) + ".txt"

try:
    new = open(os.path.join(path,namefile),"w+")

    try:
        with open(name, 'r') as f:
            print('szyfrowanie...')

            zaszyfrowany = cezar.szyfrowanie(f.read(), key)

            new.write(zaszyfrowany)
            
            print(zaszyfrowany)
    except IOError:
        print("Nie znaleziono pliku: ", name)
except IOError:
    print("Nie znaleziono katalogu")
