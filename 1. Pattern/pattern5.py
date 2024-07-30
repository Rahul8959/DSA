n= int(input("enter any muber: "))

i=1

while(i<=n):
    j = 1
    while(j<=n):
        print(chr(ord('A')+i-1), end=" ")
        j += 1
    print()
    i += 1