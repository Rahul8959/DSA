# n=3
# tmp=(n*2)-2
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ")
    
#     for j in range(tmp):
#         print(" ", end=" ")
    
#     for i in range(i+1):
#         print("*", end=" ")
    
#     tmp -= 2
#     print()

# tmp=2
# for i in range(n-1):
#     for j in range(n-i-1):
#         print("*", end=" ")
    
#     for j in range(tmp):
#         print(" ", end=" ")
    
#     for i in range(n-i-1):
#         print("*", end=" ")
    
#     tmp+=2

#     print()

n=4
tmp=(2*n-2)
for i in range(1,(2*n-1)+1):
    star = i
    if(i>n): star=(2*n)-i

    for j in range(star):
        print("*", end=" ")

    for j in range(tmp):
        print(" ", end=" ")
    
    for j in range(star):
        print("*", end=" ")
    
    if(i<n):tmp -= 2
    else: tmp += 2
    print()


    


