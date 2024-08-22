def superiorElements(a):
    ans = []
    n = len(a)
    ans.append(a[n-1])
    for i in range(n-2,-1,-1):
        if(ans[len(ans)-1]<a[i]):
            ans.append(a[i])

    ans.sort()
    return ans