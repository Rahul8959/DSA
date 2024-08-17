def alternateNumbers(a):
    # Write your code here.
    pos = []
    neg = []
    n = len(a)

    for i in range(n):
        if(a[i]>=0):
            pos.append(a[i])
        else:
            neg.append(a[i])

    if len(pos)>len(neg):
        for i in range(len(neg)):
            a[2*i]=pos[i]
            a[2*i+1]=neg[i]
        
        index = len(neg)*2
        for i in range(len(neg), len(pos)):
            a[index] = pos[i]
            index+=1
    else:
        for i in range(len(pos)):
            a[2*i]=pos[i]
            a[2*i+1]=neg[i]
        
        index = len(pos)*2
        for i in range(len(pos), len(neg)):
            a[index] = neg[i]
            index+=1
    return a

x = input("Enter array values: ")
a = [int(x) for x in x.split()]
print(alternateNumbers(a))