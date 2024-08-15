import sys
#Brute Force 
# def sub_array_sum(arr,n):
#     maxi = -sys.maxsize-1

#     for i in range(n):
#         for j in range(i,n):
#             summ=0
#             for k in range(i,j+1):
#                 summ+=arr[k]
#             maxi = max(maxi,summ)
    
#     return maxi

#Better
# def sub_array_sum(arr,n):
#     maxi = -sys.maxsize-1

#     for i in range(n):
#         summ=0
#         for j in range(i,n):
#             summ+=arr[j]
#             maxi = max(maxi,summ)
#     return maxi

#Optimized
# def sub_array_sum(arr,n):
#     maxi = -sys.maxsize-1
#     summ = 0
#     for i in range(n):
#         summ+=arr[i]

#         if(summ>maxi):
#             maxi=summ

#         if(summ<0):
#             summ=0
#     if maxi<0:
#         return 0
#     return maxi

def sub_array_sum(arr,n):
    maxi = -sys.maxsize-1
    summ = 0

    start = 0
    ansstart,ansend=-1,-1

    for i in range(n):
        if summ==0:
            start=i
        summ+=arr[i]

        if summ>maxi:
            maxi=summ
            ansstart = start
            ansend = i
        
        if summ<0:
            summ=0
    
    for i in range(ansstart,ansend+1):
        print(arr[i], end=" ")
    print()
    return maxi

x = input("Enter array values: ")
a = [int(x) for x in x.split()]
print("Maximum Subarray Sum is: ", sub_array_sum(a,len(a)))