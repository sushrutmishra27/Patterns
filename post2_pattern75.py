def pat75(n):
    for i in range(n):
        for j in range(n):
            if(j==0 or i==0 or i==n-1 or j==n-1 or i-j==0 or i+j==n-1):
                print('*',end='')
            else:
                print(" ",end='')
        print()

pat75(5)
