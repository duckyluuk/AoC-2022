import time

with open("14.txt") as f:
    start = time.time()
    data = f.read().split("\n")
    data = [[[int(x.split(",")[0])-300,int(x.split(",")[1])] for x in d.split(" -> ")] for d in data]
    maxY = max(x[1] for d in data for x in d)+1
    #print(data)
    grid = [[0 for x in range(400)] for y in range(maxY+1)]

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

    sandX=200
    sandY=0
    while sandY != maxY-1:
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
            sandX=200
            sandY=0
        if sandY >= maxY:
            grid[sandY][sandX] = 1
            count +=1
            sandX=200
            sandY=0

    res=count
    print(res)
    print(time.time()-start)

    count = 0
    for y,line in enumerate(grid):
        for x in range(200-y,200+y+1):
            if(grid[y][x] == 0):
                if y < 1 or (grid[y-1][x-1] == 1 or grid[y-1][x] == 1 or grid[y-1][x+1] == 1):
                    grid[y][x] = 1



    gridStr = "\n".join(["".join(str(x) for x in v) for v in grid])
    #print(gridStr.replace('0','.').replace("2","#").replace("1","O"))

    res2 = gridStr.count("1")
    print(res2)
    print(time.time()-start)