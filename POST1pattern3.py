n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if (i-j>=0):
            print(n-1-i+j ,end=' ')
    print('\n')

for i in range(0,n-1):
    for j in range(0,n-1):
        if (i+j<=n-2):
            print(n-3+i+j ,end=' ')
    print('\n')
