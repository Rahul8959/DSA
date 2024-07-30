n=4
for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    
    c ='A'
    tmp=(2*i+1)//2
    for j in range(2*i+1):
        print(c, end=" ")
        if j<tmp: c = chr(ord(c)+1)
        else: c = chr(ord(c)-1)


    for i in range(n-i-1):
        print(" ", end="")
    
    print()