# n=3
# for i in range(n):
#     for i in range(n-i-1):
#         print(" ", end="")
    
#     for i in range(((2*i)+1)):
#         print("*", end="")
    
#     for i in range(((n-i)-1)):
#         print(" ", end="")
    
#     print()

def pattern7(N):
    # This is the outer loop which will loop for the rows.
    for i in range(N):
        # For printing the spaces before stars in each row
        for j in range(N - i - 1):
            print(" ", end="")
        
        # For printing the stars in each row
        for j in range(2 * i + 1):
            print("*", end="")
        
        # For printing the spaces after the stars in each row
        for j in range(N - i - 1):
            print(" ", end="")
        
        # As soon as the stars for each iteration are printed, we move to the
        # next row and give a line break otherwise all stars
        # would get printed in 1 line.
        print()

# Example usage:
N = 5
pattern7(N)
