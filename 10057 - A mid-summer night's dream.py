while True:
    try:
        n = int(input())
    except EOFError:
        break

    a = sorted([int(input()) for _ in range(n)])
    x = a[(n - 1) // 2]
    y = a[n // 2]

    c = sum(1 for i in a if i == x or i == y)
    d = y - x + 1

    print(x, c, d)