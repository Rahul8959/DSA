def rotate(arr, n):
    tmp = arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]
    arr[n-1]=tmp
    return arr

x = input("Enter the array Values: ")
arr = [int(x) for x in x.split()]
print(rotate(arr,len(arr)))