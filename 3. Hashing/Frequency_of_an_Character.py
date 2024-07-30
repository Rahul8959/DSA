s = input("Enter an String: ")

has = {}

for i in range(len(s)):
    key = ord(s[i])- ord('a')
    if key in has:
        has[key] += 1
    else:
        has[key]=1

print(has)

q = int(input("Enter ant Value "))

while(q>0):
    c = input("Enter: ")
    if c in has:
        print(has[ord(c)- ord('a')])
    else:
        print(0)
    q-=1