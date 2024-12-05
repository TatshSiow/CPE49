while True:
    try:
        a, b = map(int, input().split())
        if b <= 1 or a < b:
            print("Boring!")
        else:
            result = []
            while a >= 1:
                result.append(a)
                if a == 1:
                    print(*result)
                    break
                if a % b != 0:
                    print("Boring!")
                    break
                a=a//b
    except EOFError:
      break