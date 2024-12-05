while True:
  try:
    a,b=map(int,input().split())
    if a==0 and b==0:
      break
    count=0
    carry=0
    while (a!=0 or b!=0):
      carry=0
      sum=a%10+b%10+carry
      if sum>=10:
        carry=1
        count+=1
      else:
        carry=0
      a/=10
      b/=10
    if count == 0:
      print("No carry operation.")
    elif count== 1:
      print("1 carry operation.")
    else:
      print(f"{count} carry operations.")
  except EOFError:
    break