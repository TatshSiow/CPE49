n = input()
toggle = True
result = []
for char in n:
    if char == '"':
        if toggle:
            result.append("``")
        else:
            result.append("''")
        toggle = not toggle
    else:
        result.append(char)

print("".join(result))