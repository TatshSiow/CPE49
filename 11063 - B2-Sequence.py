count=1
while True:
  try:
    n=int(input())
    a=list(map(int,input().split()))
    checker=0
    for i in range(1,n):
      if int(a[i])==int(2*(a[i-1])):
        checker=1
      else:
        checker=0
    if checker==1:
      print (f"Case #{count}: It is a B2-Sequence.")
      print()
    if checker==0:
      print (f"Case #{count}: It is not a B2-Sequence.")
      print()
    count+=1
    input()
  except EOFError:
    break