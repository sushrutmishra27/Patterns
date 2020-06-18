n=int(input())
for i in range(n):
    for j in range(n):
        if(i-j==0):
            print('0',end=' ')
        else:
            print('*',end=' ')
    print('\n')
