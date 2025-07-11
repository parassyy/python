for i in range(5,0,-1):
    for j in range(1,i+1):
        if j<=i:
            print(j,end=' ')
        else:
            print(' ',end=' ')
    print()
