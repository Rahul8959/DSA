def linear_search(arr,n,f):

    for i in range(n):
        if(arr[i]==f):
            return i
    return -1
    

x = input("Enter array items: ")
arr = [int(i) for i in x.split()]
n=len(arr)
f = int(input("Enter Value: "))

ans = linear_search(arr,n,f)

if(ans==-1):
    print("Value is not present in the array")
else:
    print("Value is Present in the array at Index: ", ans)