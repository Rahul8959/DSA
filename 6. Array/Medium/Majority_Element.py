# Brute Force
# def majority_element(arr,n):
#     for i in range(n):
#         cnt=0
#         for j in range(n):
#             if arr[i]==arr[j]:
#                 cnt+=1
#         if cnt>n//2: return arr[i]
#     return -1

#Better
# from collections import Counter

# def majority_element(arr,n):

#     count = Counter(arr)

#     for key, val in count.items():
#         if val>n//2:
#             return key
    
#     return -1
    
#optimized
def majority_element(arr,n):
    cnt = 0
    ele = None

    for i in range(n):
        if cnt == 0:
            cnt+=1
            ele=arr[i]
        elif arr[i]==ele:
            cnt+=1
        else:
            cnt-=1
    
    cnt1 = 0
    for i in range(n):
        if arr[i]==ele:
            cnt+=1
    
    if cnt>n//2:
        return ele
    else:
        return -1

x = input("Enter array values: ")
a = [int(x) for x in x.split()]
print(majority_element(a,len(a)))