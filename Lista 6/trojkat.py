def czyTrojkat(a, b, c):
    boki = [a, b, c]
    boki.sort()
    if boki[2] < boki[0] + boki[1]:
        return True
    return False
def obwodTrojkata(a, b, c):
    obwod = a + b + c
    print("Obwod trojkata: ", obwod)
def poleTrojkata(a, b, c):
    obwod = a + b + c
    pole = (a + b + c) / 2
    print("Pole trojkata: ", pole)
def zaleznoscBokowTrojkata(a, b, c):
    if a == b and a == c:
        print("Trojkat jest rownoboczny")
    elif a != b and a != c and b != c:
        print("Trojkat jest roznoboczny")
    else:
        print("Trojkat jest rownoramienny")
def zaleznoscKatowTrojkata(a, b, c):
    boki = [a, b, c]
    boki.sort()
    if boki[2] ** 2 == boki[1] ** 2 + boki[0] ** 2:
        print("Trojkat jest prostokatny")
    elif boki[2] ** 2 > boki[1] ** 2 + boki[0] ** 2:
        print("Trojkat jest rozwartokatny")
    else:
        print("Trojkat jest ostrokatny")
