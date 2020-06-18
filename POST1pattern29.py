n=int(input())
for i in range(n):
    for j in range(n-1):
        if i+j==n-1:
            print(i+1,end='')
        else:
            print(' ',end='')
    for j in range(n+1):
        if i==j:
            print(i+1,end='')
        else:
            print(' ',end='')
    print('\n')
