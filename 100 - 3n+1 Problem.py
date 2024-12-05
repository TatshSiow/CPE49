while True:
    try:
        a, b = map(int, input().split())
        max_steps = 0
        for i in range((min(a,b)),(max(a,b)) + 1):
            n = i
            count = 1
            while n > 1:
                if n % 2 == 0:
                    n = n/2
                else:
                    n = 3 * n + 1
                count += 1
            max_steps = max(max_steps, count)

        print(a, b, max_steps)
    except EOFError:
        break