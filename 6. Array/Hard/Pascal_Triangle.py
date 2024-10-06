
from typing import *

# Brute Force
# def nCr(n, r):
#     res = 1

#     # calculating nCr:
#     for i in range(r):
#         res = res * (n - i)
#         res = res // (i + 1)
#     return int(res)

# def pascalTriangle(n : int) -> List[List[int]]:
#     ans = []

#     #Store the entire pascal's triangle:
#     for row in range(1, n+1):
#         tempLst = [] # temporary list
#         for col in range(1, row+1):
#             tempLst.append(nCr(row - 1, col - 1))
#         ans.append(tempLst)
#     return ans

#Optimized
def generateRow(row):
    ans = 1
    ansRow = [1] #inserting the 1st element
    
    #calculate the rest of the elements:
    for col in range(1, row):
        ans *= (row - col)
        ans //= col
        ansRow.append(ans)
    return ansRow

def pascalTriangle(n : int) -> List[List[int]]:
    ans = []
    
    #store the entire pascal's triangle:
    for row in range(1, n+1):
        ans.append(generateRow(row))
    return ans

n = int(input("Enter: "))
ans = pascalTriangle(n)
for it in ans:
    for ele in it:
        print(ele, end=" ")
    print()
