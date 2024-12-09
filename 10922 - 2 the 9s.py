while True:
    try:
        n = input()
        if n == "0":
            break
        temp = 0
        for digit in n:
            temp += int(digit)
        if temp % 9 == 0:
            deg = 1
            while temp > 9:
                new_sum = 0
                while temp > 0:
                    new_sum += temp % 10
                    temp //= 10
                temp = new_sum
                deg += 1
            print(f"{n} is a multiple of 9 and has 9-degree {deg}.")
        else:
            print(f"{n} is not a multiple of 9.")
    except EOFError:
        break