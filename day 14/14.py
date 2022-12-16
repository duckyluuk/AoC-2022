import time

with open(__file__.split('\\')[-1].replace("py","txt")) as f:
    start = time.time()
    data = f.read().split("\n")
    data = [[[int(x.split(",")[0])-200,int(x.split(",")[1])] for x in d.split(" -> ")] for d in data]
    maxY = max(x[1] for d in data for x in d)+1
    print(maxY)
    #print(data)
    grid = [[0 for x in range(600)] for y in range(maxY+1)]

    for line in data:
        x=y=0
        for point in line:
            if(x and y):
                for px in range(min(x,point[0]),max(x+1,point[0]+1)):
                    for py in range(min(y,point[1]),max(y+1,point[1]+1)):
                        grid[py][px]=2
            x=point[0]
            y=point[1]


    count = 0
    res = 0

    sandX=300
    sandY=0
    while grid[0][300]==0:
        if grid[sandY+1][sandX] == 0:
            sandY+=1
        elif grid[sandY+1][sandX-1] == 0:
            sandY+=1
            sandX-=1
        elif grid[sandY+1][sandX+1] == 0:
            sandY+=1
            sandX+=1
        else:
            grid[sandY][sandX] = 1
            count +=1
            sandX=300
            sandY=0
        if sandY >= maxY:
            grid[sandY][sandX] = 1
            count +=1
            sandX=300
            sandY=0
        
        if not res and sandY==maxY-1:
            res=count
            print(res)
            print(time.time()-start)

    #print("\n".join(["".join(str(x) for x in v) for v in grid]).replace('0','.').replace("2","#").replace("1","O"))
    
    res2 = count
    print(res2)
    print(time.time()-start)