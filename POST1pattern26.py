n=int(input())
m=65
for i in range(n):
    for j in range(n-1-i):
        print(' ',end='')
    for j in range(i+1):
        print(chr(m+i) ,end=' ')
    print('\n')
for i in range(n-1):
    for j in range(i+1):
        print(' ',end='')
    for j in range(n-i-1):
        print(chr(m+n-2-i) ,end=' ')
    print('\n')
        
