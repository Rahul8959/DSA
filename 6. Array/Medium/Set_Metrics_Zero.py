def markRow(matrix,m,n,i):
    for j in range(m):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def markCol(matrix,m,n,j):
    for i in range(n):
        if matrix[i][j] != 0:
            matrix[i][j] =-1

def zeroMatrix(matrix,n,m):

    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                markRow(matrix,m,n,i)
                markCol(matrix,m,n,j)
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==-1:
                matrix[i][j]=0
    
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