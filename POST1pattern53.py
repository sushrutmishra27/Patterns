n=int(input())
for i in range(n):
    for j in range(n):
        if (i-j==0):
            print( n-i ,end=' ')
        elif (i+j==n-1):
            print(i+1,end=' ')
        else:
            print(' ',end=' ')
    print('\n')
