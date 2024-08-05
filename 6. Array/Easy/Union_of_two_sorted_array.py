#Brute force
# def union_array(arr1,arr2,n,m):
#     s = set()

#     for i in range(n):
#         s.add(arr1[i])
    
#     for i in range(m):
#         s.add(arr2[i])

#     s = list(s)
#     s.sort()

#     return s

def sortedArray(a, b):
    # Write your code here
    n1 = len(a)
    n2 = len(b)
    i = 0
    j = 0
    unionArr = []
    while(i<n1 and j<n2):
        if(a[i]<=b[j]):
            if(len(unionArr)==0 or unionArr[-1]!=a[i]):
                unionArr.append(a[i])
            i+=1
        else:
            if(len(unionArr)==0 or unionArr[-1]!=b[j]):
                unionArr.append(b[j])
            j+=1
    
    while(i<n1):
        if(len(unionArr)==0 or unionArr[-1]!=a[i]):
            unionArr.append(a[i])
        i+=1
    while(j<n2):
        if(len(unionArr)==0 or unionArr[-1]!=b[j]):
            unionArr.append(b[j])
        j+=1
    
    return unionArr

x = input("Enter array 1 items: ")
arr1 = [int(i) for i in x.split()]
n = len(arr1)

x = input("Enter array 2 items: ")
arr2 = [int(i) for i in x.split()]
m = len(arr2)

print("Union of sorted array is: ", sortedArray(arr1,arr2))
