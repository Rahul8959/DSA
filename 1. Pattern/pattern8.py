n = int(input("enter any mnumber: "))

i=1
while(i<=n):
    #it will print the space first
    space = n-i
    while(space):
        print(" ", end=" ")
        space -= 1
    
    j=1
    while(j<=i):
        print("*", end=" ")
        j += 1

    print()
    i+=1