s = 'abcdffs'
has = {}
for i in range(len(s)):
    key = ord(s[i])- ord('a')
    has[key]+=1