def write_list(list):
    print(' '.join([str(item) for item in list]).center(100))

x = input("Podaj liczbe poziomow: ")
line = [1]
write_list(line)
for i in range(int(x) - 1):
    line = [1] + [x + y for x, y in zip(line[1:], line[:-1])] + [1]
    write_list(line)
