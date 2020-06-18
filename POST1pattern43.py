"""
n=int(input())
for i in range(n):
    for j in range(n):
        if(i+j<=n-1):
            print('*',end='')
        else:
            print('',end='')
    print('\n')

    for j in range():
        print('', end='')
    for j in range(0,n-1-i):
        print('*', end='')
    print('\n')
"""
n=int(input())
for i in range(n):
    for j in range(n-1):
        if i+j<=n-1:
            print('*',end='')
        else:
            print(' ',end='')
    for j in range(n):
        if i-j<=0:
            print('*',end='')
        else:
            print(' ',end='')
    print('\n')
