
# def sum_num(n, sum):
#     if(n<1):
#         print(sum)
#         return
    
#     sum_num(n-1, sum+n)

# sum_num(3,0)

def number_sum(n):
    if(n==1):
        return 1
    
    return(n+number_sum(n-1))

print(number_sum(3))