def biggestCommonDividor(a,b):
    l_divisor = 0
    if b>a:
        [a,b] = [b,a]
    for i in range(2,a):
        if a % i == 0 and b%i ==0:
            l_divisor = i
    return l_divisor
print(biggestCommonDividor(-122,18))