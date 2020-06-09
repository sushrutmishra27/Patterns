n=int(input())
for i in range(n):
    for j in range(n-1-i):
        print(' ',end='')
    for j in range(i+1):
        print(j+1,end=' ')
        j+=1
    print('\n')
