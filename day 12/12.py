import time

with open(__file__.split('\\')[-1].replace("py","txt")) as f:
    start = time.time()
    data = f.read()

    letters='abcdefghijklmnopqrstuvwxyz'

    map=[list(x) for x in data.split("\n")]
    p2Starts=[]

    startY = data.index("S")//(len(map[0])+1)
    startX = data.index("S")%(len(map[0])+1)
    map[startY][startX] = "a"

    endY = data.index("E")//(len(map[0])+1)
    endX = data.index("E")%(len(map[0])+1)
    map[endY][endX] = "z"

    for y,row in enumerate(map):
        for x,spot in enumerate(row):
            if spot=="a":
                p2Starts.append([x,y,0])

    def search(positions):
        checked=[]
        while positions:
            p=positions.pop(0)
            x,y,dis = p
            pos = [x,y]

            if(pos == [endX,endY]):
                return dis
            if not pos in checked:
                checked.append(pos)
                
                diffs=[[1,0],[0,1],[-1,0],[0,-1]]
                for d in diffs:
                    nx,ny=x+d[0],y+d[1]
                    if 0<=nx<len(map[0]) and 0<=ny<len(map) and letters.index(map[ny][nx])-letters.index(map[y][x])<=1:
                        positions.append([nx,ny,dis+1])

    res = search([[startX,startY,0]])
    print(res)
    print(time.time()-start)
    
    res2 = search(p2Starts)
    print(res2)
    print(time.time()-start)