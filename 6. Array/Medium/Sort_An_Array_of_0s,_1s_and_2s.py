# Brute Force
# def sort012(arr,n):
#     cnt0,cnt1,cnt2=0,0,0

#     for num in arr:
#         if num==0:
#             cnt0+=1
#         elif num==1:
#             cnt1+=1
#         else: 
#             cnt2+=1
    
#     for i in range(cnt0): arr[i]=0
#     for i in range(cnt0, cnt0+cnt1): arr[i]=1
#     for i in range(cnt0+cnt1, n): arr[i]=2

#optimized
def sort012(arr,n):
    low = 0
    mid = 0
    high = n-1

    while(mid<=high):
        if(arr[mid]==0):
            arr[low], arr[mid] = arr[mid], arr[low]
            mid+=1
            low+=1
        elif (arr[mid]==1):
            mid+=1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high-=1

x = input("Enter array values: ")
a = [int(x) for x in x.split()]
sort012(a, len(a))
print("Sorted Array is: ", a)