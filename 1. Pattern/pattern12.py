n = 4

for i in range(n-1,-1,-1):
    for j in range(n-i-1):
        print(" ", end="")
    
    for j in range(2*i+1):
        print("*", end="")

    for j in range(n-i+1):
        print(" ", end="")
    
    print()
