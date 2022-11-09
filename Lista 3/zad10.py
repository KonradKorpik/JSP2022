for x in range(200, 401):
    if (x // 100) % 2 == 0:
        if (x // 10) % 2 == 0:
            if x % 2 == 0:
                print(x, end=", ")
