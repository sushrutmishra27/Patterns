n=int(input())
for i in range(n):
    for j in range(2*n):
        if (i+j>=n-1 and j<n) or (i+j-n>=n-1 and j>=n):
            print('* ',end='')
        elif (j<n and i+j<=n):
            print(' ',end='')
        else:
            print('  ',end='')
    print('\n')
        
