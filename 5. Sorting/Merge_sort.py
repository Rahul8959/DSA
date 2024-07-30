def merge(arr,low,mid,high):
    tmp = []
    left = low
    right = mid+1

    while(left<=mid and right<=high):
        if(arr[left]<=arr[right]):
            tmp.append(arr[left])
            left+=1
        else:
            tmp.append(arr[right])
            right+=1
    
    while(left<=mid):
        tmp.append(arr[left])
        left+=1
    
    while(right<=high):
        tmp.append(arr[right])
        right+=1
    # print(tmp)
    for i in range(low,high+1):
        arr[i]=tmp[i-low]


def merge_sort(arr, low, high):
    if(low>=high):
        return
    mid = (low+high)//2
    merge_sort(arr,low,mid) 
    merge_sort(arr,mid+1,high)
    merge(arr,low,mid,high)



x = input("Enter the Array Values: ")
arr = [int(val) for val in x.split()]
n = len(arr)
merge_sort(arr, 0, n-1)
print(arr)