import math
while True:
  try:
    a,b=map(int,input().split())
    square=0
    if a+b==0:
      break
    for i in range(a,b+1):
      if int(math.sqrt(i))==math.sqrt(i):
        square+=1
    print(square)
  except EOFError:
    break