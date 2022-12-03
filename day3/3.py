import time

with open(__file__.split('\\')[-1].replace("py","txt")) as f:
    start = time.time()
    data = f.read().split("\n")
    
    chars = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    res = 0
    for d in data:
        size=len(d)
        a,b=d[:size//2],d[size//2:]
        both=list(set(a)&set(b))[0]
        res+=chars.index(both)
    
    print(res)
    print(time.time()-start)
    
    res2 = 0
    for d in range(0,len(data),3):
        both=list(set(data[d])&set(data[d+1])&set(data[d+2]))[0]
        res2+=chars.index(both)
    print(res2)
    print(time.time()-start)