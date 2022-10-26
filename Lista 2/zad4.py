napis = input()
znak = napis[0]
napis = napis.replace(znak, "$")
napis = list(napis)
napis[0] = znak
napis = "".join(napis)

print(napis)
