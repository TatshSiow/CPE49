c = 0
while True:
	try:
		n = input()
	except EOFError:
		break
	freq = [0] * 256
	for char in n:
		freq[ord(char)] += 1
	if c > 0:
		print()
	c += 1
	for count in range(1, len(n) + 1):
		for i in range(255, -1, -1):
			if freq[i] == count:
				print(i, count)