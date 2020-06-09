n=int(input())
for i in range(n):
    for j in range(n-1-i):
        print(' ',end='')
    for j in range(i+1):
        print(i+1 ,end=' ')
    print('\n')
for i in range(n-1):
    for j in range(i+1):
        print(' ',end='')
    for j in range(n-i-1):
        print(n-1-i ,end=' ')
    print('\n')
        
