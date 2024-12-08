import math
T = int(input())
for t in range(T):
	s = input()
	l = input()
	s, l = int(s, 2), int(l, 2)
	if math.gcd(s, l) > 1:
		print(f'Pair #{t+1}: All you need is love!')
	else:
		print(f'Pair #{t+1}: Love is not all you need!')