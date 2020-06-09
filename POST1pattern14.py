n=int(input())
m=65
for i in range(n):
    for j in range(n-1-i):
        print(' ',end='')
    for j in range(i+1):
        print(chr(m+i),end=' ')
        j+=1
    print('\n')
