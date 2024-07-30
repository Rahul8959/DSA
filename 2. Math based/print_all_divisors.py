from math import *
# lst = []
n=36
# for i in range(1,n+1):
#     # print(i, end=" ")
#     if(n%i==0):
#         lst.append(i)

lst = []
for i in range(1,int(sqrt(n))+1):
    if(n%i==0):
        lst.append(i)
        if(n//i!=i):
            lst.append(n//i)
print(lst.sort())
lst = lst.sort()
print(lst)
# for i in lst:
#     print(i, end=" ")