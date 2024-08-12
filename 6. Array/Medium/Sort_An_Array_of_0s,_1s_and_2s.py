def sort012(arr,n):

    cnt0,cnt1,cnt2=0,0,0

    for num in arr:
        if num==0:
            cnt0+=1
        elif num==1:
            cnt1+=1
        else: 
            cnt2+=1
    
    for i in range(cnt0): arr[i]=0
    for i in range(cnt0, cnt0+cnt1): arr[i]=1
    for i in range(cnt0+cnt1, n): arr[i]=2

x = input("Enter array values: ")
a = [int(x) for x in x.split()]
sort012(a, len(a))
print("Sorted Array is: ", a)