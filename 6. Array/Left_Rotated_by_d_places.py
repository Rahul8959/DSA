#Brute Force
# def left_rotate(arr, n ,d):
#     d = d%n
#     tmp=[]
#     for i in range(d):
#         tmp.append(arr[i])
    
#     for i in range(d,n):
#         arr[i-d]=arr[i]
    
#     for i in range(n-d,n):
#         arr[i] = tmp[i-(n-d)]
    
#     return arr

#Optimized Aproach
def reverse_array(arr,start, end):
    end-=1
    while(start<=end):
        arr[start], arr[end] = arr[end], arr[start]
        start+=1
        end-=1

def left_rotate(arr,n,d):
    d=d%n
    reverse_array(arr,0,d)
    reverse_array(arr,d,n)
    reverse_array(arr,0 ,n)
    return arr


x = input("Enter: ")
arr = [int(x) for x in x.split()]
n = len(arr)
d = int(input("Enter D: "))
print(left_rotate(arr,n,d))
