from collections import defaultdict
# Better
# def findAllSubarraysWithGivenSum(arr, s):
#     # Write your code here.
#     n = len(arr)
#     cnt = 0
#     ans = 0
#     for i in range(n):
#         summ = 0
#         for j in range(i,n):
#             summ += arr[j]
#             if summ==s:
#                 cnt+=1
#     return cnt

#Optimized
def findAllSubarraysWithGivenSum(arr, k):
    n = len(arr) # size of the given array.
    mpp = defaultdict(int)
    preSum = 0
    cnt = 0

    mpp[0] = 1 # Setting 0 in the map.
    for i in range(n):
        # add current element to prefix Sum:
        preSum += arr[i]

        # Calculate x-k:
        remove = preSum - k

        # Add the number of subarrays to be removed:
        cnt += mpp[remove]

        # Update the count of prefix sum
        # in the map.
        mpp[preSum] += 1

    return cnt

x = input("Enter the list: ")
arr = [int(x) for x in x.split()]
s = int(input("Enter K: "))
ans = findAllSubarraysWithGivenSum(arr, s)

print(f"Count of Subarrays that sum is {s}: {ans}")
