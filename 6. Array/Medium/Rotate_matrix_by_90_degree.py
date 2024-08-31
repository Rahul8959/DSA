# Brute Force
# def rotate(matrix):
#     n = len(matrix)
#     rotated = [[0 for _ in range(n)] for _ in range(n)]

#     for i in range(n):
#         for j in range(n):
#             rotated[j][n-1-i]=matrix[i][j]

#     for i in range(n):
#         for j in range(n):
#             matrix[i][j] = rotated[i][j]

#Optimized
def rotate(mat):
    # Write your code here.
    n = len(mat)

    #Transpose the matrix
    for i in range(n):
        for j in range(i):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    
    #Reverse the row
    for i in range(n):
        mat[i].reverse()

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

rotate(example_matrix)

print("Rotated matrix is:")
for row in example_matrix:
    for ele in row:
        print(ele, end=" ")
    print()