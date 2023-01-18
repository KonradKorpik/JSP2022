from itertools import combinations

class trzyElem():
    lista = []

    def __init__(self, lista):
        self.lista = lista
    def trzymEle(self):
        kombinacje = list(combinations(self.lista, 3))
        wyniki = []

        for i in kombinacje:
            if sum(i) == 0:
                wyniki.append(list(i))
        return wyniki

test = trzyElem([1, -3, 4, 1, 2, 0, 7, 2, 5, -2, -4, -1])

print(test.trzymEle())
