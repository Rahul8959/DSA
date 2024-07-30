# def pindex(arr, low, high):
#     pivot = arr[low]
#     i = low
#     j=high

#     while(i<j):
#         while(arr[i]<=pivot and i<high):
#             i+=1
#         while(arr[j]>pivot and j>low):
#             j-=1
#         if(i<j):
#             arr[i],arr[j] = arr[j],arr[i]
    
#     arr[low], arr[j] = arr[j], arr[low]
#     return j

# def quick_sort(arr, low, high):
#     if(low<high):
#         pi = pindex(arr, low, high)
#         quick_sort(arr,low, pi-1)
#         quick_sort(arr,pi+1,high)

# x = input("Enter the Array Values: ")
# arr = [int(val) for val in x.split()]
# n = len(arr)
# quick_sort(arr, 0, n-1)
# print(arr)

def pindex(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while arr[i] <= pivot and i < high:
            i += 1
        while arr[j] > pivot and j > low:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sort(arr, low, high, depth=0):
    if low < high:
        pi = pindex(arr, low, high)
        print(f"Iteration {depth}: {arr} with pivot index {pi} (pivot value {arr[pi]})")
        quick_sort(arr, low, pi - 1, depth + 1)
        quick_sort(arr, pi + 1, high, depth + 1)

x = input("Enter the Array Values: ")
arr = [int(val) for val in x.split()]
n = len(arr)
quick_sort(arr, 0, n - 1)
print("Sorted Array:", arr)
