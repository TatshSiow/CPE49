n=int(input())

for i in range(n):
  a=int(input())
  b=int(input())
  c=0
  for j in range (a,b+1):
    if j%2!=0:
      c+=j
  print(f'Case {i+1}: {c}')