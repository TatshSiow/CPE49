while True:
    try:
        a = input().strip()
        b = input().strip()
        a_sorted = sorted(a)
        b_sorted = sorted(b)
        result = []
        for char in a_sorted:
            if char in b_sorted:
                result.append(char)
                b_sorted.remove(char)
        print(''.join(result))
    except EOFError:
        break