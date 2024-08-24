# Brute Froce
# def linear_search(a,num):
#     n = len(a)

#     for i in range(n):
#         if a[i]==num:
#             return True
#     return False

# def Longest_successive(arr):
#     n = len(arr)
#     longest = 1

#     for i in range(n):
#         x = arr[i]
#         cnt=1
#         while linear_search(arr, x+1):
#             x+=1
#             cnt+=1
#         longest = max(longest,cnt)
#     return longest

#better
# def Longest_successive(arr):
#     # Write your code here. 
#     n = len(arr)
#     if n==0:
#         return 0
    
#     arr.sort()
#     cnt=0
#     lastsmall = float('-inf')
#     longest = 1

#     for i in range(n):
#         if (arr[i]-1 == lastsmall):
#              cnt+=1
#              lastsmall=arr[i]
#         elif (arr[i]!=lastsmall):
#             cnt=1
#             lastsmall=arr[i]
#         longest = max(longest,cnt)
#     return longest

#Optimized
def Longest_successive(arr):
    n = len(arr)
    if n==0:
        return 0
    
    longest = 1
    st = set()

    for num in arr:
        st.add(num)

    for num in st:
        if num-1 not in st:
            cnt=1
            x=num

            while(x+1 in st):
                cnt+=1
                x+=1
            longest = max(cnt,longest)

    return longest

x = input("Enter array values: ")
a = [int(x) for x in x.split()]
print(Longest_successive(a))