
n=int(input())
m=65
for i in range(n):
    for j in range(n-1-i):
        print(' ',end='')
    for j in range(i+1):
        print(chr(m+j) ,end=' ')
    print('\n')
for i in range(n-1):
    for j in range(i+1):
        print(' ',end='')
    for j in range(n-i-1):
        print(chr(m+i+1+j) ,end=' ')
    print('\n')
        
