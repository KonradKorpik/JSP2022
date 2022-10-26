lista = ["Kasia", "Basia", "Marek", "Darek"]
lista.append("Józek")
lista.extend(["Ania", "Basia"])
lista = sorted(lista)

print(lista)
print((lista[3]))
print(lista[:2])
print(lista[-2:])

lista.remove("Basia")

print(lista)
print(len(lista))

lista = tuple(lista)

print(lista)
