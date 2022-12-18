import time

with open(__file__.split('\\')[-1].replace("py","txt")) as f:
    start = time.time()
    data = f.read().split("\n")

    grid = [[[0 for z in range(26)] for y in range(26)] for x in range(26)]

    for d in data:
        x,y,z=list(map(int,d.split(",")))
        x,y,z=x+2,y+2,z+2
        #print(a,b,c)
        grid[x][y][z]=1

    dir = [[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]]

    res=0
    first = False
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            for z in range(len(grid[x][y])):
                if(grid[x][y][z]):
                    for d in dir:
                        nx=x+d[0]
                        ny=y+d[1]
                        nz=z+d[2]
                        if(grid[nx][ny][nz]==0):
                            if not first: first=[nx,ny,nz]
                            res+=1

    print(res)
    print(time.time()-start)

    def search(positions):
        count=0
        checked=[]
        while positions:
            position = positions.pop(0)
            if position[:3] in checked: continue

            checked.append(position[:3])

            for d in dir:
                nx,ny,nz=position[0]+d[0],position[1]+d[1],position[2]+d[2]
                if 0<=nx<25 and 0<=ny<25 and 0<=nz<25:
                    newPos = [nx,ny,nz]
                    if grid[nx][ny][nz] == 0:
                        found=False
                        for d in dir:
                            cx=nx+d[0]
                            cy=ny+d[1]
                            cz=nz+d[2]
                            if(grid[cx][cy][cz]==1):
                                found=True
                                break
                        
                        if(found): positions.append(newPos+[1])
                        else:
                            if position[3]>0: positions.append(newPos+[position[3]-1])
                    else: 
                        count+=1
        return count

    res2=search([first+[1]])                                

    print(res2)
    print(time.time()-start)