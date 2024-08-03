def move_zeros(arr,n):
    
    tmp = []

    for i in range(n):
        if(arr[i] != 0):
            tmp.append(arr[i])
    
    for i in range(len(tmp)):
        arr[i]=tmp[i]
    
    for i in range(len(tmp), n):
        arr[i]=0
    
    return arr



x = input("Enter array items: ")
arr = [int(i) for i in x.split()]
print(move_zeros(arr, len(arr)))