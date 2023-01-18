from bs4 import BeautifulSoup 

with open("kursy.xml", "rb") as file:
    dane = file.read()
    dane_bs4 = BeautifulSoup(dane, "xml")
 
pozycje = dane_bs4.find_all('pozycja')
waluty = []

for pozycja in pozycje:
    waluta = []
    nazwa_waluty = pozycja.find("nazwa_waluty").text
    przelicznik = pozycja.find("przelicznik").text
    kod_waluty = pozycja.find("kod_waluty").text
    kurs_sredni = pozycja.find("kurs_sredni").text
    waluta.append(nazwa_waluty)
    waluta.append(przelicznik)
    waluta.append(kod_waluty)
    waluta.append(kurs_sredni)
    waluty.append(waluta)

def listaDostepnychKursow():
    for i in range(0, len(waluty)):
        print("Kod waluty: " + waluty[i][2] + " Kurs waluty: " + waluty[i][3])
def zamianaKrajowa(n, kodWaluty):
    for i in range(0, len(waluty)):
        if kodWaluty == waluty[i][2]:
            kurs = waluty[i][3]
            kurs = kurs.split(",")
            kurs = float(kurs[0] + "." + kurs[1])

            print(n / kurs, kodWaluty)

            break
def zamianaMiedzynarodowa(n, kodWaluty1, kodWaluty2):
    for i in range(0, len(waluty)):
        if kodWaluty1 == waluty[i][2]:
            kurs1 = waluty[i][3]
            kurs1 = kurs1.split(",")
            kurs1 = float(kurs1[0] + "." + kurs1[1])
        if kodWaluty2 == waluty[i][2]:
            kurs2 = waluty[i][3]
            kurs2 = kurs2.split(",")
            kurs2 = float(kurs2[0] + "." + kurs2[1])
            
    print((n * kurs1) / kurs2, kodWaluty2)

listaDostepnychKursow()
zamianaKrajowa(1000, "USD")
zamianaMiedzynarodowa(1000, "EUR", "USD")
