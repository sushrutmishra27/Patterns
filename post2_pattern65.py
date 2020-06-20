n=int(input())
for i in range(n):
    for j in range(n):
        if i+j>=n-1:
            print('*',end='')
        elif i%2==0 and j==n-2-i:
            print('*',end='')
        else:
            print(' ',end='')
    print('\n')
