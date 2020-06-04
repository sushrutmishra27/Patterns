n=int(input())
m=n+65-1
for i in range(n):
    for j in range(n):
        if (i-j>=0):
            print(chr(m-j) ,end=' ')
    print('\n')

for i in range(0,n-1):
    for j in range(0,n-1):
        if (i+j<=n-2):
            print(chr(m-j) ,end=' ')
    print('\n')







def pos_neg(a, b, negative):
  if(((a<0 and b>0) or (a>0 and b<0)) and not negative):
    return True
  elif (negative and a<0 and b<0):
    return True
  else:
    return False
  
