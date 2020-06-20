n=int(input())
for i in range(n):
    for j in range(n):
        if i-j<=0:
            print('* ',end='')
        elif i%2!=0 and j==i-1:
            print('* ',end='')
        else:
            print('  ',end='')
    print('\n')
