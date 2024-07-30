N=5
def printNos(N):
    #Your code here
    if(N<=0):
        return
    print(N, end=" ") 
    printNos(N-1)
    

printNos(N)