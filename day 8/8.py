import time

with open(__file__.split('\\')[-1].replace("py","txt")) as f:
    start = time.time()
    data = [[int(x) for x in list(d)] for d in f.read().split("\n")]
    res = 0
    visible = [[0 for x in range(len(data[0]))] for y in data]

    def checkTree(x,y,d,h):
        if(data[y][x]>h):visible[y][x]=1
        h=max(data[y][x],h)
        nx,ny=x+d[0],y+d[1]
        if(nx>=0 and nx<99 and ny>=0 and ny<99): checkTree(nx,ny,d,h)

    for n in range(99):
        checkTree(0,n,[1,0],-1)
        checkTree(98,n,[-1,0],-1)
        checkTree(n,0,[0,1],-1)
        checkTree(n,98,[0,-1],-1)
        
    #print("\n".join(["".join(str(x) for x in v) for v in visible]))

    for y in visible:
        for x in y:
            if(x>0): res+=1

    print(res)
    print(time.time()-start)
    
    res2 = 0

    def findScore(x,y,h):
        l=r=u=d=0
        
        for nx in range(x-1,-1,-1):
            l+=1
            if(data[y][nx]>=h): break
        for nx in range(x+1,99):
            r+=1
            if(data[y][nx]>=h): break
        for ny in range(y-1,-1,-1):
            u+=1
            if(data[ny][x]>=h): break
        for ny in range(y+1,99):
            d+=1
            if(data[ny][x]>=h): break

        s = l * r * u * d
        return s

    for x in range(99):
        for y in range(99):
            h = data[y][x]
            score = findScore(x,y,h)
            res2 = max(res2,score)

    print(res2)
    print(time.time()-start)