# Brute force
# def two_sum(a,n,k):

#     for i in range(n):
#         for j in range(i+1,n):
#             if(a[i]+a[j]==k):
#                 return [i,j]
                
#     return -1

# def two_sum(a,n,k):
#     hash_map ={}
    
#     for i in range(n):
#         diff = k-a[i]
#         if diff in hash_map:
#             return [i, hash_map[diff]]
#         else:
#             hash_map[a[i]]=i
#     return -1

def two_sum(a,n,k):
    left = 0
    right = n-1
    a.sort()

    for i in range(n):
        Sum = a[left]+a[right]
        if(Sum==k):
            return "YES"
        elif(Sum<k):
            left+=1
        else:
            right-=1
    return -1

x = input("Enter array values: ")
n = int(input("Enter Value: "))
a = [int(x) for x in x.split()]
ans = two_sum(a,len(a),n)
if ans==-1:
    print("Sum values are not present.")
else:
    print("Sum Values are present at index", ans)