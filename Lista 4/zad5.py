import itertools

def f(lista):
    p = list(itertools.permutations(lista))
    print(p)

f([1, 2, 3])
