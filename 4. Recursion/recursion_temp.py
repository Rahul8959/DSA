cnt=0

def fun():
    global cnt
    
    if(cnt==4): return
    else: print(cnt)

    cnt+=1
    fun()

fun()