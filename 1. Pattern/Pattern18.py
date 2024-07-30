n=5
inis=0
for i in range(n):
    for j in range(n-i):
        print("*", end="")
    
    for j in range(inis):
        print(" ", end="")
    
    for j in range(n-i):
        print("*", end="")
    
    inis+=2
    print()
inis = 2 * n - 2
for i in range(1,n+1):
    for j in range(i):
        print("*", end="")
    
    for j in range(inis):
        print(" ", end="")
    
    for j in range(i):
        print("*", end="")
    
    inis-=2
    print()

# def pattern19(N):
#     # for the upper half of the pattern.
    
#     # initial spaces.
#     iniS = 0
#     for i in range(N):
        
#         # for printing the stars in the row.
#         for j in range(N - i):
#             print("*", end="")
        
#         # for printing the spaces in the row.
#         for j in range(iniS):
#             print(" ", end="")
        
#         # for printing the stars in the row.
#         for j in range(N - i):
#             print("*", end="")
        
#         # The spaces increase by 2 every time we hit a new row.
#         iniS += 2
        
#         # As soon as the stars for each iteration are printed, we move to the
#         # next row and give a line break otherwise all stars
#         # would get printed in 1 line.
#         print()
    
#     # for lower half of the pattern
    
#     # initial spaces.
#     iniS = 2 * N - 2
#     for i in range(1, N + 1):
        
#         # for printing the stars in the row.
#         for j in range(i):
#             print("*", end="")
        
#         # for printing the spaces in the row.
#         for j in range(iniS):
#             print(" ", end="")
        
#         # for printing the stars in the row.
#         for j in range(i):
#             print("*", end="")
        
#         # The spaces decrease by 2 every time we hit a new row.
#         iniS -= 2
        
#         # As soon as the stars for each iteration are printed, we move to the
#         # next row and give a line break otherwise all stars
#         # would get printed in 1 line.
#         print()

# # Example usage:
# pattern19(5)

