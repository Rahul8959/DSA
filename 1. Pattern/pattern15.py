n=4
tmp=1
for i in range(n+1):
    for j in range(i):
        print(tmp, end=" ")
        tmp+=1
    
    print()