import trojkat as tr

a = float(input("Podaj bok a: "))
b = float(input("Podaj bok b: "))
c = float(input("Podaj bok c: "))

if tr.czyTrojkat(a, b, c) == False:
    print("Z podanych bokow, nie da sie stworzyc trojkata!")
else:
    tr.obwodTrojkata(a, b, c)
    tr.poleTrojkata(a, b, c)
    tr.zaleznoscBokowTrojkata(a, b, c)
    tr.zaleznoscKatowTrojkata(a, b, c)
