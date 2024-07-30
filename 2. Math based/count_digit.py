# n = 12
# count=0
# i=n
# while(i>0):
#     # print("while")
#     tmp=i%10
#     print("tmp: ",tmp)
#     i=i//10
#     print("i: ", i)
    
#     if(n%tmp==0):
#         count+=1
#     print()
#     print("count: ", count)

# # print(n%2)
# print("ANS: ",count)
# # print(n)
# # print(i)

import math
n = 45345
ans = int(math.log10(n)) + 1

print("Answer: ", ans)