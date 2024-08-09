# Brute Force
# def longest_subarray(arr,n,k):
#     l = 0
#     for i in range(n):
#         s = 0
#         for j in range(i, n):
#             s+=arr[j]
#             if(s==k):
#                 l = max(l,j-i+1)
                
#     return l

#Better
def longest_subarray(a, n, k):

    preSumMap = {}
    Sum = 0
    maxLen = 0
    for i in range(n):
        # calculate the prefix sum till index i:
        Sum += a[i]

        # if the sum = k, update the maxLen:
        if Sum == k:
            maxLen = max(maxLen, i + 1)

        # calculate the sum of remaining part i.e. x-k:
        rem = Sum - k

        # Calculate the length and update maxLen:
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)

        # Finally, update the map checking the conditions:
        if Sum not in preSumMap:
            preSumMap[Sum] = i

    return maxLen

x = input("Enter array items: ")
arr = [int(i) for i in x.split()]
n=len(arr)
k = int(input("Enter K Value: "))
print("Longest subarray is: ", longest_subarray(arr,n,k))