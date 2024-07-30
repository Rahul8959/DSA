n = int(input("Enter Any Number: "))

i = 1
while(i<=n):
    j=1
    while(j<=i):
        print(chr(ord('A')+i+j-2), end=" ")
        j+=1
    print()
    i+=1