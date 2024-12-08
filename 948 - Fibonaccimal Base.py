t = int(input())
for _ in range(t):
	num = int(input())
	n = num
	fibs = [1, 2]
	result = []
	while fibs[-1] <= n:
		fibs.append(fibs[-1] + fibs[-2])
	for fib in reversed(fibs[:-1]):
		if fib <= n:
			result.append('1')
			n -= fib
		else:
			result.append('0')
	print(f"{num} = {''.join(result).lstrip('0')} (fib)")