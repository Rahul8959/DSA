#Brute force
# def superiorElements(a):
#     ans= []
#     n=len(a)

#     for i in range(n):
#         leader = True
#         for j in range(i+1,n):
#             if(a[i]<a[j]):
#                 leader = False
#                 break
#         if leader:
#             ans.append(a[i])
#     ans.reverse()
#     return ans

#optimized
def superiorElements(a):
    ans = []
    n = len(a)
    ans.append(a[n-1])
    for i in range(n-2,-1,-1):
        if(ans[len(ans)-1]<a[i]):
            ans.append(a[i])

    ans.reverse()
    return ans

x = input("Enter array values: ")
a = [int(x) for x in x.split()]
print(superiorElements(a))