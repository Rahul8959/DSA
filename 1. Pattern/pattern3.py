n = int(input("Enter Any Number: "))

# i=1
# count = 0
# while(i<=n):
#     j=1
#     count = i
#     while(j<=i):
#         print(count, end=" ")
#         count += 1
#         j += 1
#     print()
#     i += 1

#without using count variable
i=0
while(i<n+1):
    j=0
    while(j<i):
        print(i+j, end=" ")
        j += 1
    print()
    i += 1

