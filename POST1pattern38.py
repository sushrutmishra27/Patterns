n=int(input())
for i in range(n):
    for j in range(n-1):
        if i+j==n-1:
            print(' *',end='')
        else:
            print('  ',end='')
    for j in range(n+1):
        if i==j:
            print(' *',end='')
        else:
            print('  ',end='')
    print('\n')

for i in range(n-1):
    for j in range(n-2):
        if i==j:
            print('  *',end='')
        else:
            print('  ',end='')
    for j in range(n):
        if i+j==n-1:
            print(' *',end='')
        else:
            print('  ',end='')
    print('\n')
