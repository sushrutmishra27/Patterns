n=int(input())
m=65
for i in range(0,n):
    for j in range(i):
        print(' ',end='')
    for j in range(n-i):
        print(chr(m+j),end=' ')
    print('\n')
