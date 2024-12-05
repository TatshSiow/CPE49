n = int(input())

for i in range(n):
  a,b = map(int,input().split())

  if (a+b) %2 or (a-b)<0:
    print('impossible')
  else:
    print(int((a+b)/2),int((a-b)/2))