arr = [2,6,6,2,3,2,3,5,7,7,7,7]
n = len(arr)

m={}

for i in arr:
    if i in m:
        m[i]+=1
    else:
        m[i]=1

h = arr[0]
l = arr[n-1]
val_h = 0
val_l = 0
for i in m:
    if m[i]<l:
        l=m[i]
        val_l = i
    elif m[i]>h:
        h=m[i]
        val_h=i
print(m)
print(val_h,": ", h)
print(val_l,": ", l)