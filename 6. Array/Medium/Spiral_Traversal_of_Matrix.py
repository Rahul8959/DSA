def printSpiral(mat):
    # Define ans array to store the result.
    ans = []
 
    n = len(mat) # no. of rows
    m = len(mat[0]) # no. of columns
  
    # Initialize the pointers reqd for traversal.
    top = 0
    left = 0
    bottom = n - 1
    right = m - 1

    # Loop until all elements are not traversed.
    while (top <= bottom and left <= right):
        # For moving left to right
        for i in range(left, right + 1):
            ans.append(mat[top][i])

        top += 1

        # For moving top to bottom.
        for i in range(top, bottom + 1):
            ans.append(mat[i][right])

        right -= 1

        # For moving right to left.
        if (top <= bottom):
            for i in range(right, left - 1, -1):
                ans.append(mat[bottom][i])

            bottom -= 1

        # For moving bottom to top.
        if (left <= right):
            for i in range(bottom, top - 1, -1):
                ans.append(mat[i][left])

            left += 1

    return ans

Rows = int(input("Give the number of rows: "))  
Columns = int(input("Give the number of columns: "))  
  
# Initializing the matrix  
example_matrix = []  
print("Please give the entries row-wise:")  
  
# For user input  
for _ in range(Rows):  # This for loop is to arrange rows  
    # Take the input for the entire row and split it into a list of integers
    r = list(map(int, input().split()))
    # Append the row to the matrix
    example_matrix.append(r)  
                     
ans = printSpiral(example_matrix)

print(ans)