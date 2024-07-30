def bubble_sort(arr, n):
    if(n==1):
        return
    swapped = False
    for i in range(n-1):
        if(arr[i]>arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]
            swapped = True
    if not swapped:
        return
    
    # print(n,": ",arr)
    bubble_sort(arr, n-1)
    

x = input("Enter the Array Values: ")
arr = [int(val) for val in x.split()]
bubble_sort(arr, len(arr))
print(arr)