from matplotlib.pyplot import xlabel


x = list(range(3, 100, 3))
print(x)
del x[4::3]
print(x)
srednia = sum(x)/len(x)
print(srednia)
