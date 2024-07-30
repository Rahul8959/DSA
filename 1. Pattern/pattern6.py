n = int(input("enter any number: "))

i=1
while(i<=n):
    j=1
    while(j<=n):
        print(chr(ord("A")+i+j-2),end=" ")
        j+=1
    print()
    i+=1