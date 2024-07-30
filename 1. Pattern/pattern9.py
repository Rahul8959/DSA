n = int(input("Enter any Number: "))

i=1
while(n>=0):
    j=1
    while(j<=n):
        print("*", end=" ")
        j+=1

    print()
    n -= 1