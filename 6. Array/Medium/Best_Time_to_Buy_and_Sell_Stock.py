def maximumProfit(prices):
    # Write your code here.
    n=len(prices)
    maxi = 0
    pricecost = 0
    mini = prices[0]
    for i in range(1,n):
        pricecost = prices[i]-mini
        maxi = max(maxi,pricecost)
        mini = min(mini,prices[i])
    return maxi

x = input("Enter array values: ")
a = [int(x) for x in x.split()]
print(maximumProfit(a))