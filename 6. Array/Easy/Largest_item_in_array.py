def largest(arr,n):
    tmp = arr[0]
    for i in range(n):
        if(tmp<arr[i]):
            tmp=arr[i]
    return tmp

x = input("Enter array items: ")
arr = [int(i) for i in x.split()]
print(largest(arr,len(arr)))