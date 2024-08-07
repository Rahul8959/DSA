# Brute force
# def single_num(arr,n):
#     for i in range(n):
#         num = arr[i]
#         cnt=0
#         for j in range(n):
#             if(arr[j] == num):
#                 cnt+=1

#         if cnt==1:
#             return num

#Better
# def single_num(arr):
#     hash_map ={}

#     for num in arr:
#         if num in hash_map:
#             hash_map[num]+=1
#         else:
#             hash_map[num]=1
    
#     for key in hash_map:
#         if hash_map[key]==1:
#             return key

#Optimized
def single_num(arr):
    xor = 0
    for num in arr:
        xor = xor^num
    return xor

x = input("Enter array items: ")
arr = [int(i) for i in x.split()]
print(single_num(arr))
