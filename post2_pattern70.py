n=int(input())
c=n
for i in range(2*n):
    if i%2==0 and c!=0:
        c-=1
    for k in range(n-c):
        print(' ',end=' ')
    for j in range(c):
        print('*',end=' ')
    print('\n')
