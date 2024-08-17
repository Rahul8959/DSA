#Brute Fore
#  def alternateNumbers(a):
#     # Write your code here.
#     pos = []
#     neg = []
#     n = len(a)

#     for i in range(n):
#         if(a[i]>=0):
#             pos.append(a[i])
#         else:
#             neg.append(a[i])

#     for i in range(n//2):
#         a[2*i]=pos[i]
#         a[2*i+1]=neg[i]
#     return a

#optimized
def alternateNumbers(nums):
    posi=0
    negi=1
    n = len(nums)
    ans = [0]*n
    for i in range(n):
        if nums[i]<0:
            ans[negi] = nums[i]
            negi+=2
        else:
            ans[posi] = nums[i]
            posi+=2
    return ans
x = input("Enter array values: ")
a = [int(x) for x in x.split()]
print(alternateNumbers(a))