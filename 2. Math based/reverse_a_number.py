n = int(input("Enter Any Number: "))

tmp=0
ans=0
while(n>-1):
    tmp = n%10
    n=n//10
    ans=ans*10+tmp

print("Answer: ", ans)

print(-123<-1)