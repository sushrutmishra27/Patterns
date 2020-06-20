n=int(input())
k=1
for i in range(n):
    
    for j in range(n):
        if i-j>=0 and j<k:
            print('* ',end='')            
        else:
            print(' ',end='')
    if((i+1)%2==0):
        k=k+1
    print('\n')
