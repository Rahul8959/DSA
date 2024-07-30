n=int(input("Enter: "))
for i in range(n):
    for j in range(n-i):
        print(" ", end="")

    for j in range(i):
        print(chr(ord('A')+j), end="")

    for j in range(i,-1,-1):
        # print(j)
        print(chr(ord('A')+j), end="")
    
    print()

# for j in range(2,-1,-1):
#     # print(j)
#     print(j," : ",chr(ord('A')+j))