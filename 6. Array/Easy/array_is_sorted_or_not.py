def check_sorted(arr,n):
    for i in range(1,n):
        if(arr[i-1]>arr[i]):
            return False
    return True

x = input("Enter array items: ")
arr = [int(i) for i in x.split()]

if(check_sorted(arr,len(arr))):
    print("Array is Sorted")
else:
    print("Array is Not Sorted")