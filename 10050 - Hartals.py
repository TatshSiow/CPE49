T = int(input())
for _ in range(T):
    days = int(input())
    n = int(input())
    party = [int(input()) for _ in range(n)] 
    strike = set()
    for i in party:
        for temp in range(i, days+1, i):
            if temp % 7!=6 and temp%7!=0:
                strike.add(temp)
    print(len(strike))