def consecutive(a, n):
    maxi = 0
    cnt = 0

    for i in range(n):
        if(a[i]==1):
            cnt+=1
            if(cnt>maxi):
                maxi=cnt
        else:
            cnt=0
        
    return maxi

x = input("Enter array items: ")
arr = [int(i) for i in x.split()]
n=len(arr)
print("Answer: ", consecutive(arr,n))