n=int(input())
m=65
for i in range(n):
    for j in range(n):
        if (i-j==0):
            print(chr(m+i) ,end=' ')
        elif (i+j==n-1):
            print(chr(m+n-1-i),end=' ')
        else:
            print(' ',end=' ')
    print('\n')
