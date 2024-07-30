a=15  
b=16
# for i in range(min(a,b),-1,-1):
#     if(a%i==0 and b%i==0):
#         # print(a,b)
#         print(i)
#         break

while(a>0 and b>0):
    if(a>b): a=a%b
    else: b=b%a


if(a==0):print(b)
else: print(a)