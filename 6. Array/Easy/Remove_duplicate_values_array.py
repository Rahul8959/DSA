#Brute Force Approach
# def duplicated(arr,n):
#     s=set()
#     for i in range(n):
#         s.add(arr[i])
#     return list(s)

#Optimized Approach
def duplicated(arr,n):
    i=0
    for j in range(1,n):
        if(arr[j]!=arr[i]):
            arr[i+1] = arr[j]
            i+=1
    return arr[:i+1]

x = input("Enter array items: ")
arr = [int(i) for i in x.split()]

arr = duplicated(arr, len(arr))
print(arr)
