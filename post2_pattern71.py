n=int(input())
c=0
for i in range(2*n):
    if i%2==0:
        c+=1
    for k in range(n-c):
        print(' ',end=' ')
    for j in range(2*c-1):
        print('*',end=' ')
    print()
