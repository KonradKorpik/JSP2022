while(1):
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))

    if b < a:
        Z = b % a
        Z *= Z + 3
        print(Z)
        break
    
    else:
        print("Liczba a musi byc wieksza od liczby b")
