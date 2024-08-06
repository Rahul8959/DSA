def sortedArray(arr1,n,arr2,m):
    i = 0
    j = 0
    ans = []

    while(i<n and j<m):
        if(arr1[i]<arr2[j]):
            i+=1
        elif(arr2[j]<arr1[i]):
            j+=1
        else:
            ans.append(arr1[i])
            i+=1
            j+=1
    
    return ans

x = input("Enter array 1 items: ")
arr1 = [int(i) for i in x.split()]
n = len(arr1)

x = input("Enter array 2 items: ")
arr2 = [int(i) for i in x.split()]
m = len(arr2)

print("Intersection of sorted array is: ", sortedArray(arr1, n, arr2, m))