n = int(input("Enter: "))
i=1

while(i<=n):
    space=i-1
    while(space):
        print(" ",end=" ")
        space -=1
    
    j=1
    while(j<=n-i+1):
        print("*", end=" ")
        j+=1

    print()
    i+=1
