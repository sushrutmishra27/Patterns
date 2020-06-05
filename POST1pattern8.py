n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if i+j>=n-1:
            print(j ,end=' ')
        else:
            print('  ',end='')
    print('\n')

for i in range(0,n-1):
    for j in range(0,n):
        if i-j<0:
            print(j,end=' ')
        else:
            print('  ',end='')
    print('\n')
