n=int(input())
m=65
for i in range(0,n):
    for j in range(0,n):
        if i+j>=n-1:
            print(chr(m+j) ,end=' ')
        else:
            print('  ',end='')
    print('\n')

for i in range(0,n-1):
    for j in range(0,n):
        if i-j<0:
            print(chr(m+j),end=' ')
        else:
            print('  ',end='')
    print('\n')
