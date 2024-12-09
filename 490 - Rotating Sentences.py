lines = []
while True:
	try:
		line = input()
		lines.append(line)
		max_length = 0
	except EOFError:
		break

for line in lines:
	if len(line) > max_length:
		max_length = len(line)

for col in range(max_length):
	row = ""
	for line in reversed(lines):
		if col < len(line):
			row += line[col]
		else:
			row += " "
	print(row)