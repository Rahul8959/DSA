def insertion_sort(arr, n, i=0):
    if i==n:
        return
    
    j = i
    while(j>0 and arr[j-1]>arr[j]):
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j-=1

    insertion_sort(arr,n,i+1)

x = input("Enter the Array Values: ")
arr = [int(val) for val in x.split()]
n = len(arr)
insertion_sort(arr, n)
print(arr)