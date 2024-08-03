#brute Force
# def right_rotate(arr, n, d):
#     d=d%n
#     if d==0: return arr
#     for i in range(d):
#         tmp = arr[n-1]
#         for j in range(n-2,-1,-1):
#             arr[j+1]=arr[j]
#         arr[0]=tmp
    
#     return arr

def reverse_array(arr,start, end):
    end-=1
    while(start<=end):
        arr[start], arr[end] = arr[end], arr[start]
        start+=1
        end-=1

def right_rotate(arr,n,k):
    k=k%n
    if k==0: return arr

    reverse_array(arr,0,n-k)
    reverse_array(arr,n-k,n)
    reverse_array(arr,0,n)

    return arr


x = input("Enter the array Values: ")
arr = [int(x) for x in x.split()]
k = int(input("Enter D: "))
print(right_rotate(arr,len(arr),k))