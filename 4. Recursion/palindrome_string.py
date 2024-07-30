def palindrome(s,i=0):
    s=s.lower()
    if(i>=len(s)//2):
        return "Palindrome"
    elif(s[i]!=s[len(s)-i-1]):
        return "Not Palindrome"
    return palindrome(s,i+1)


print(palindrome("A man, a plan, a canal: Panama"))

tmp = ("A man, a plan, a canal: Panama123").lower()

tmp=tmp.replace(" ", "")
print(tmp)
print(tmp[::-1])