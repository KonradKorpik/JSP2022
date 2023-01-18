from itertools import combinations, chain

class Podlisty():
    def __init__(self, lista):
        self.lista = lista
    def podlisty(self):
        kombinacje = [combinations(self.lista, i) for i in range(len(self.lista) + 1)]
        wynik = chain(*kombinacje)
        wynik = [list(i) for i in wynik]

        return wynik

x = Podlisty([1, 3, 4, 2])

print(x.podlisty())
