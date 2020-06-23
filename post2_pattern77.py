n=int(input())
s=0
k=1
for i in range(n):
    for j in range(n):
        if i-j>=0:
            b=s+k
            print(b,end=' ')
            s=k
            k=b
        else:
            print('',end=' ')
    print('\n')

