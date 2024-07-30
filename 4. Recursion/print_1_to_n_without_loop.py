N=5
def printNos(N):
    #Your code here
    if(N<=0):
        return

    printNos(N-1)
    print(N, end=" ") 

printNos(N)
