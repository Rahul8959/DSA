def bubble_sort(arr,n):
    for i in range(n-2,-1,-1):
        didswap = False
        for j in range(i+1):
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                didswap = True
        if(didswap == False):
            break
        print(i, ": ", arr)

n = int(input("Enter the Size of array: "))
x = input("Enter the Array Values: ")
arr = [int(val) for val in x.split()]
bubble_sort(arr, n)
print(arr)
