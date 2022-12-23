import time

with open(__file__.split('\\')[-1].replace("py","txt")) as f:
    start = time.time()
    mapData,instructions = f.read().split("\n\n")
    instructions+=" "
    w = max(len(x) for x in mapData.split("\n")) + 1
    grid = [[" " for x in range(w)],*[[x for x in " "+row.ljust(w," ")] for row in mapData.split("\n")],[" " for x in range(w)]]

    #print(grid)

    pos = [grid[1].index("."),1]
    directions = [[1,0],[0,1],[-1,0],[0,-1]]
    d=0

    i=0
    num=""
    while i<len(instructions):
        #print(i)
        if instructions[i].isnumeric():
            num+=instructions[i]
        else:
            #print(num, instructions[i])
            num=int(num)
            for x in range(num):
                newPos = [pos[0]+directions[d][0],pos[1]+directions[d][1]]
                if grid[newPos[1]][newPos[0]] == " ":
                    row = grid[newPos[1]]
                    if d==0:
                        newPos[0] = min(row.index("."),row.index("#") if "#" in row else 9999)
                    if d==2:
                        newPos[0] = max(len(row)-row[::-1].index(".")-1,len(row)-row[::-1].index("#")-1 if "#" in row else 0)

                    col = [line[newPos[0]] for line in grid]
                    if d==1:
                        newPos[1] = min(col.index("."),col.index("#") if "#" in col else 9999)
                    if d==3:
                        newPos[1] = max(len(col)-col[::-1].index(".")-1,len(col)-col[::-1].index("#")-1 if "#" in col else 0)

                if grid[newPos[1]][newPos[0]] == ".":
                    pos = newPos
            
            num=""
            if instructions[i]=="R":
                d=(d+1)%4
            if instructions[i]=="L": d=(d-1)%4
        i+=1

    res = pos[1]*1000+pos[0]*4+d
    print(res)
    print(time.time()-start)

    grid = [[x for x in row.ljust(w-1," ")] for row in mapData.split("\n")]

    faces = []

    size = 50

    for y in range(0,len(grid),size):
        for x in range(0,len(grid[y]),size):
            faces.append([row[x:x+size] for row in grid[y:y+size]])


    faces = list(filter(lambda x: x[0][0] != " ", faces))
    face = 0
    pos = [0,0]

    faceMoves = [
        {"U":{"face":5,"side":"L"},"L":{"face":3,"side":"L"},"R":{"face":1,"side":"L"},"D":{"face":2,"side":"U"}},
        {"U":{"face":5,"side":"D"},"L":{"face":0,"side":"R"},"R":{"face":4,"side":"R"},"D":{"face":2,"side":"R"}},
        {"U":{"face":0,"side":"D"},"L":{"face":3,"side":"U"},"R":{"face":1,"side":"D"},"D":{"face":4,"side":"U"}},
        {"U":{"face":2,"side":"L"},"L":{"face":0,"side":"L"},"R":{"face":4,"side":"L"},"D":{"face":5,"side":"U"}},
        {"U":{"face":2,"side":"D"},"L":{"face":3,"side":"R"},"R":{"face":1,"side":"R"},"D":{"face":5,"side":"R"}},
        {"U":{"face":3,"side":"D"},"L":{"face":0,"side":"U"},"R":{"face":4,"side":"D"},"D":{"face":1,"side":"U"}}
    ]
    facePositions = [
        [1,0],
        [2,0],
        [1,1],
        [0,2],
        [1,2],
        [0,3]
    ]

    def checkMove(pos, move, face, d):
        newPos = [pos[0]+move[0], pos[1]+move[1]]
        off = False
        on = False
        newFace = face
        if newPos[0] < 0:
            off = "L"
            newFace = faceMoves[face][off]["face"]
            on = faceMoves[face][off]["side"]
            
            if on == "L": newPos = [0,size-newPos[1]-1]
            if on == "R": newPos = [size-1,newPos[1]]
            if on == "U": newPos = [newPos[1],0]
            if on == "D": newPos = [size-newPos[1]-1,size-1]

        elif newPos[0] >= size:
            off = "R"
            newFace = faceMoves[face][off]["face"]
            on = faceMoves[face][off]["side"]

            if on == "L": newPos = [0,newPos[1]]
            if on == "R": newPos = [size-1,size-newPos[1]-1]
            if on == "U": newPos = [size-newPos[1]-1,0]
            if on == "D": newPos = [newPos[1],size-1]

        elif newPos[1] < 0:
            off = "U"
            newFace = faceMoves[face][off]["face"]
            on = faceMoves[face][off]["side"]

            if on == "L": newPos = [0,newPos[0]]
            if on == "R": newPos = [size-1,size-newPos[0]-1]
            if on == "U": newPos = [size-newPos[0]-1,0]
            if on == "D": newPos = [newPos[0],size-1]
            
        elif newPos[1] >= size:
            off = "D"
            newFace = faceMoves[face][off]["face"]
            on = faceMoves[face][off]["side"]

            if on == "L": newPos = [0,size-newPos[0]-1]
            if on == "R": newPos = [size-1,newPos[0]]
            if on == "U": newPos = [newPos[0],0]
            if on == "D": newPos = [size-newPos[0]-1,size-1]

        newD = d
        if on == "L": newD=0 
        if on == "U": newD=1
        if on == "R": newD=2
        if on == "D": newD=3


        if faces[newFace][newPos[1]][newPos[0]] == "#":
            return face,pos,d
        else:
            return newFace,newPos,newD

    d=0
    i=0
    num=""
    while i<len(instructions):
        #print(i)
        if instructions[i].isnumeric():
            num+=instructions[i]
        else:
            #print(num, instructions[i])
            num=int(num)
            for x in range(num):
                face,pos,d = checkMove(pos,directions[d],face,d)
            
            num=""
            if instructions[i]=="R":
                d=(d+1)%4
            if instructions[i]=="L": d=(d-1)%4

            #print(pos[1]+facePositions[face][1]*size,pos[0]+facePositions[face][0]*size,d)
        i+=1
    print(face,pos)
    res2 = (pos[1]+facePositions[face][1]*size+1)*1000+(pos[0]+facePositions[face][0]*size+1)*4+d
    print(res2)
    print(time.time()-start)