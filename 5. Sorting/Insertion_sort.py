def insertion_sort(arr, n):
    for i in range(n):
        j=i 
        while(j>0 and arr[j-1]>arr[j]):
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j-=1
        print(i,": ", arr)

x = input("Enter the Array Values: ")
arr = [int(val) for val in x.split()]
insertion_sort(arr, len(arr))
print("Sorted array:\n",arr)