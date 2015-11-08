def hs(n):
    index = 1
    print(n)
    while (n != 1 and n != 0):
        index = index + 1
        if n % 2:
            n = (n*3) + 1
        else:
            n = n//2
        print(n)
    print(index)
