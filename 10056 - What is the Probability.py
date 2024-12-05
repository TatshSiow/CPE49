T = int(input())
for _ in range(T):
    numbers, chance, success = input().split()
    numbers, chance, success = int(numbers), float(chance), int(success)
    fail = 1 - chance
    if chance == 0:
        print('0.0000')
    else:
        print(f'{chance * (fail ** (success - 1)) / (1 - fail ** numbers):.4f}')