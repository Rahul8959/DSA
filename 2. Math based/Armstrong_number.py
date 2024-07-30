def isArmstrong(num):
    # Write your code here.
    dup = num
    ans = 0

    while(num>0):
        tmp = num%10
        num = num//10
        ans = ans+(tmp**3)
    print(ans,dup)
    if(dup==ans): print('YES')
    else: print('NO')

isArmstrong(1634)