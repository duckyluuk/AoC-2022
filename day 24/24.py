import time  

def updategrid(grid,data):
    newgrid = [[{"wall":x=="#","blizzards":[]} for x in d] for d in data]
    for y,row in enumerate(grid):
        for x,space in enumerate(row):
            for b in space["blizzards"]:
                nx = x+b[0]
                ny = y+b[1]

                if nx < 1: nx = len(row)-2
                if ny < 1: ny = len(grid)-2
                if nx > len(row)-2: nx = 1
                if ny > len(grid)-2: ny = 1

                newgrid[ny][nx]["blizzards"].append(b)
    
    return newgrid

checked = []
def getMoves(grid, x, y):
    possibleMoves = []
    for d in [[1,0],[-1,0],[0,1],[0,-1],[0,0]]:
        nx = x+d[0]
        ny = y+d[1]
        #print(nx,ny)
        if 0<=nx<len(grid[0]) and 0<=ny<len(grid):
            if not grid[ny][nx]["wall"] and len(grid[ny][nx]["blizzards"]) == 0:
                possibleMoves.append([nx,ny])
    
    return possibleMoves
def search(grid, x, y, goal, data):
    possibleMoves = [[x,y,0]]
    newPossibleMoves = possibleMoves
    while newPossibleMoves:
        grid = updategrid(grid,data)
        #print(possibleMoves[0][2])
        newPossibleMoves = []
        while possibleMoves:
            x,y,t=possibleMoves.pop()
            newMoves = getMoves(grid,x,y)
            for m in newMoves:
                if m == goal: return grid,t+1

                if not [m[0],m[1],t+1] in newPossibleMoves: 
                    newPossibleMoves.append([m[0],m[1],t+1])
        possibleMoves = newPossibleMoves


with open("24.txt") as f:
    start = time.time()
    data = f.read().split("\n")
    dirSymbols = {">":[1,0],"<":[-1,0],"^":[0,-1],"v":[0,1],"#":0,".":0}

    grid = [[{"wall":x=="#","blizzards":list(filter(lambda c: c,[dirSymbols[x]]))} for x in d] for d in data]
    pos = [1,0]
    goal = [len(grid[0])-2,len(grid)-1]
    
    grid,res = search(grid,pos[0],pos[1],goal,data)
    print(res)
    print(time.time()-start)
    
    grid,r = search(grid,goal[0],goal[1],pos,data)
    grid,r2 = search(grid,pos[0],pos[1],goal,data)
    
    res2 = res+r+r2
    print(res2)
    print(time.time()-start)