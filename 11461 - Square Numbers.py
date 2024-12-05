while True:
  a,b=map(int,input().split())
  if a==0 and b==0:
    break
  counter = 0
  for i in range (a,b+1):
    if int(i**0.5)**2==i:
      counter +=1
  print (counter)