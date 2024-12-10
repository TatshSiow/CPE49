n = int(input())
for _ in range(n):
    a = input()
    dec2bin = bin(int(a))
    hex2bin = bin(int(a, 16))
    x1 = dec2bin.count('1')
    x2 = hex2bin.count('1')
    print(x1, x2)