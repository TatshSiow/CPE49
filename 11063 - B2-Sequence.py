case=1
while True:
  try:
    n=int(input())
    a=list(map(int,input().split()))
    check=0
    for i in range(1,n):
      if int(2*(a[i-1]))==int(a[i]):
        check=1
      else:
        check=0
    if check==1:
      print (f"Case #{case}: It is a B2-Sequence.")
    if check==0:
      print (f"Case #{case}: It is not a B2-Sequence.")
    print()
    case+=1
    input()
  except EOFError:
    break