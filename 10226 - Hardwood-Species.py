import sys
from collections import Counter

a = int(input())

for t in range(a):
    ts = []
    if t == 0: input()
    elif t != 0: print()
    while True:
        try:
            t = sys.stdin.readline().strip()
            if not t:
                c = Counter(ts)
                l = len(ts)
                ans = [f'{i} {c[i] / l * 100:.4f}' for i in sorted(c)]
                print('\n'.join(ans))
                break
            ts.append(t)
        except EOFError:
            break