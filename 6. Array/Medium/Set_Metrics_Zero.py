# Brute Force
# def markRow(matrix,m,n,i):
#     for j in range(m):
#         if matrix[i][j] != 0:
#             matrix[i][j] = -1

# def markCol(matrix,m,n,j):
#     for i in range(n):
#         if matrix[i][j] != 0:
#             matrix[i][j] =-1

# def zeroMatrix(matrix,n,m):

#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j]==0:
#                 markRow(matrix,m,n,i)
#                 markCol(matrix,m,n,j)
    
#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j]==-1:
#                 matrix[i][j]=0
    
#     return matrix

#Better
# def zeroMatrix(matrix, n, m):
#     # Write your code here.
#     row = [0]*n
#     col = [0]*m

#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j]==0:
#                 row[i]=1
#                 col[j]=1
    
#     for i in range(n):
#         for j in range(m):
#             if row[i]==1 or col[j]==1:
#                 matrix[i][j]=0
#     return matrix

#optimized
def zeroMatrix(matrix, n, m):
    col0 = 1

    # First pass: Use the first row and first column to mark zeros
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                # Mark the i-th row
                matrix[i][0] = 0
                # Mark the j-th column
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0

    # Second pass: Use the marks to set elements to zero
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Set the first row to zero if needed
    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0

    # Set the first column to zero if needed
    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0

    # Optionally return the matrix (not necessary if modifying in-place)
    return matrix

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

ans = zeroMatrix(example_matrix, Rows, Columns)


print("The Final matrix is:")
for row in ans:
    for ele in row:
        print(ele, end=" ")
    print()