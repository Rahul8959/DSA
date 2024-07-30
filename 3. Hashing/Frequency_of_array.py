def frequencyCount(arr, N):
    # code here\
    hash_map = {}
    for num in arr:
        if num in hash_map:
            hash_map[num] +=1
        else:
            hash_map[num] = 1
    # print(hash_map)
    # print()
    print(hash_map)
    for i in hash_map:
        print(i, ": ",hash_map[i])
    
    for i in range(1, N+1):
        if i in hash_map:
            arr[i-1] = hash_map[i]
        else:
            arr[i-1] = 0
        # print(i,": ", arr)

arr = [2,6,6,2,3,2,3,5,7,7,7,7]
N=len(arr)
# print("Array: ", arr)
frequencyCount(arr,N)
# print(arr)