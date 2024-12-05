n = int(input())

for _ in range(n):
    a = input()
    dex2bin = bin(int(a))[2:]
    hex2bin = bin(int(a, 16))[2:]
    x1 = dex2bin.count('1')
    x2 = hex2bin.count('1')
    print(x1, x2)