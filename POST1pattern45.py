n=int(input())
for i in range(n):
    for j in range(n):
        if i-j>=0:
            print('*',end='')
        else:
            print(' ',end='')
    for j in range(n):
        if i+j>=n-1:
            print('*',end='')
        else:
            print(' ',end='')
    
    print('\n')
for i in range(n-1):
    for j in range(n):
        if i+j+1<=n-1:
            print('*',end='')
        else:
            print(' ',end='')
    for j in range(n):
        if i-j+1<=0:
            print('*',end='')
        else:
            print(' ',end='')
    print('\n')
