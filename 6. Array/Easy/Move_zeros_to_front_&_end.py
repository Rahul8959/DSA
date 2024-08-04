#Brute Force
# def move_zeros(arr,n):
    
#     tmp = []

#     for i in range(n):
#         if(arr[i] != 0):
#             tmp.append(arr[i])
    
#     for i in range(len(tmp)):
#         arr[i]=tmp[i]
    
#     for i in range(len(tmp), n):
#         arr[i]=0
    
#     return arr

def move_zeros_to_end(arr,n):
    j=-1

    for i in range(n):
        if arr[i]==0:
            j=i
            break
    
    if(j==-1): return arr

    for i in range(j+1,n):
        if(arr[i]!=0):
            arr[j],arr[i]=arr[i],arr[j]
            j+=1

    return arr

def move_zeros_to_front(arr, n):
    j = -1
    for i in range(n-1,-1,-1):
        if arr[i] == 0:
            j = i
            break
    
    if j == -1: return arr
    
    for i in range(j-1, -1,-1):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j -= 1

    return arr


x = input("Enter array items: ")
arr = [int(i) for i in x.split()]
print(move_zeros_to_end(arr, len(arr)))
print(move_zeros_to_front(arr, len(arr)))