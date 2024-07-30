n = int(input())

arr = input()
lst=[]
lst = [int(x) for x in arr.split()]

def rev(n,lst,i=0):
    if(i>=n/2):
        return
    lst[i], lst[n-i-1] = lst[n-i-1], lst[i]
    return rev(n,lst,i+1)
    
rev(n,lst)
for i in lst:
    print(i, end=" ")