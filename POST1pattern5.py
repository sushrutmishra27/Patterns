

n=int(input())
m=n+65
for i in range(n):
    for j in range(n):
        if (i-j>=0):
            print(chr(m-1-i+j) ,end=' ')
    print('\n')

for i in range(0,n-1):
    for j in range(0,n-1):
        if (i+j<=n-2):
            print(chr(m-3+i+j) ,end=' ')
    print('\n')
