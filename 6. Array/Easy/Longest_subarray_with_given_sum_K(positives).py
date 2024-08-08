def longest_sunarray(arr,n,k):
    l = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s+=arr[j]
            if(s==k):
                l = max(l,j-i+1)
                
    return l

x = input("Enter array items: ")
arr = [int(i) for i in x.split()]
n=len(arr)
k = int(input("Enter K Value: "))
print("Longest subarray is: ", longest_sunarray(arr,n,k))