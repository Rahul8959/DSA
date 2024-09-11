def findAllSubarraysWithGivenSum(arr, s):
    # Write your code here.
    n = len(arr)
    cnt = 0
    ans = 0
    for i in range(n):
        summ = 0
        for j in range(i,n):
            summ += arr[j]
            if summ==s:
                cnt+=1
    return cnt

x = input("Enter the list: ")
arr = [int(x) for x in x.split()]
s = int(input("Enter K: "))
ans = findAllSubarraysWithGivenSum(arr, s)

print(f"Count of Subarrays that sum is {s}: {ans}")
