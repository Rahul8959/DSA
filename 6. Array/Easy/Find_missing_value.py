#Brute Force
# def find_missing(a,n):

#     for i in range(1,n+1):
#         flag = 0
#         for j in range(n-1):
#             if a[j]==i:
#                 flag = 1
#                 break
#         if flag == 0:
#             return i

#Better
# def find_missing(a,n):

#     h = [0]*(n+1)

#     for num in a:
#         h[num] = 1

#     for i in range(1,n+1):
#         if h[i]==0:
#             return i 

# first optimized
# def find_missing(a,n):

#     s = sum(a)
#     n = n*(n+1)/2
#     return int(n-s)

#second optimized
def find_missing(a,n):
    xor1= 0
    xor2= 0
    l = len(a)
    for i in range(l-1):
        xor2 = xor2^a[i]
        xor1 = xor1^(i+1)
    
    xor1 = xor1^n
    return xor1^xor2

n = int(input("Enter the Number of range: "))
x = input("Enter: ")
a = [int(x) for x in x.split()]
print("Missing Value is: ", find_missing(a,n+1))