n=int(input())
k=1
for i in range(n):
    for j in range(n):
        if i-j>=0:
            print(k,end=' ')
            k+=1
        else:
            print('',end=' ')
    print('\n')
            
