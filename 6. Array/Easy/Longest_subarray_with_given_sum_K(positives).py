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
# def longest_subarray(a, n, k):

#     preSumMap = {}
#     Sum = 0
#     maxLen = 0
#     for i in range(n):
#         # calculate the prefix sum till index i:
#         Sum += a[i]

#         # if the sum = k, update the maxLen:
#         if Sum == k:
#             maxLen = max(maxLen, i + 1)

#         # calculate the sum of remaining part i.e. x-k:
#         rem = Sum - k

#         # Calculate the length and update maxLen:
#         if rem in preSumMap:
#             length = i - preSumMap[rem]
#             maxLen = max(maxLen, length)

#         # Finally, update the map checking the conditions:
#         if Sum not in preSumMap:
#             preSumMap[Sum] = i

#     return maxLen

def longest_subarray(a,n, k):
    left, right = 0, 0 # 2 pointers
    Sum = a[0]
    maxLen = 0
    while right < n:
        # if sum > k, reduce the subarray from left
        # until sum becomes less or equal to k:
        while left <= right and Sum > k:
            Sum -= a[left]
            left += 1

        # if sum = k, update the maxLen i.e. answer:
        if Sum == k:
            maxLen = max(maxLen, right - left + 1)

        # Move forward the right pointer:
        right += 1
        if right < n: Sum += a[right]
    return maxLen

x = input("Enter array items: ")
arr = [int(i) for i in x.split()]
n=len(arr)
k = int(input("Enter K Value: "))
print("Longest subarray is: ", longest_subarray(arr,n,k))