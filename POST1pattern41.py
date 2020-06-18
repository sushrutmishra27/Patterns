n=int(input())
m=65
for i in range(n):
    for j in range(n-1):
        if i+j==n-1:
            print(chr(m+i),end='')
        else:
            print(' ',end='')
    for j in range(n+1):
        if i==j:
            print(chr(m+i),end='')
        else:
            print(' ',end='')
    print('\n')
for i in range(n-1):
    for j in range(n-2):
        if i==j:
            print(chr(m+n-i-2),end='')
        else:
            print(' ',end='')
    for j in range(n):
        if i+j==n-1:
            print(chr(m+n-i-2),end='')
        else:
            print(' ',end='')
    print('\n')
