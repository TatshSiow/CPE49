import math
def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(math.sqrt(n)) + 1))

while True:
    try:
        n = int(input())
        n_s = int(str(n)[::-1])
        if is_prime(n) and n_s != n and is_prime(n_s):
            print(f"{n} is emirp.")
        elif is_prime(n):
            print(f"{n} is prime.")
        else:
            print(f"{n} is not prime.")
    except EOFError:
        break