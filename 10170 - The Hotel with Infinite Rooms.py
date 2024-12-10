import math
while True:
    try:
        s, d = list(map(int, input().split()))
        result = int(math.ceil((-1 + ((1 - 4 * (-(s ** 2) + s - 2 * d))) ** 0.5) / 2))
        print(result)
    except EOFError:
        break