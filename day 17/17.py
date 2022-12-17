import time

with open(__file__.split('\\')[-1].replace("py","txt")) as f:
    start = time.time()
    moves = f.read()
    
    shapes = [[[2,3],[3,3],[4,3],[5,3]],
              [[3,1],[2,2],[3,2],[4,2],[3,3]],
              [[2,3],[3,3],[4,3],[4,2],[4,1]],
              [[2,0],[2,1],[2,2],[2,3]],
              [[2,3],[2,2],[3,2],[3,3]]]


    grid = [[1 for x in range(7)]]

    operation=0

    block = 0
    extraHeight = 0
    checked={}

    while block < 1000000000000:
        for y in range(len(grid)):
            if(sum(grid[y]) > 0):
                height=y-7
                break
        for i in range(-height):
            grid.insert(0,[0 for x in range(7)])
        shape=shapes[block%5]
        positions = shape


        drop = True
        while drop:
            newPositions = [[p[0]+{"<":-1,">":1}[moves[operation]],p[1]] for p in positions]
            for p in range(len(positions)):
                if newPositions[p][0] < 0 or newPositions[p][0]>6 or grid[newPositions[p][1]][newPositions[p][0]] == 1:
                    break
            else: 
                positions = newPositions
            
            newPositions = [[p[0],p[1]+1] for p in positions]
            for p in range(len(positions)):
                if grid[newPositions[p][1]][newPositions[p][0]] == 1:
                    drop = False
                    break
            else:
                positions = newPositions
            
            if not drop:
                for p in positions:
                    grid[p[1]][p[0]] = 1

            operation = (operation+1)%len(moves)
    
        if block==2021:
            res = len([x for x in grid if sum(x)]) - 1

            print(res)
            print(time.time()-start)

        checkHeight = 25

        gridStr =str(grid[:checkHeight])
        if (operation, block%5, gridStr) in checked and block > 2022:
            h1 = len(grid)
            grid = grid[:checkHeight]
            h2 = checked[operation, block%5, gridStr][1]

            oldIndex = checked[operation, block%5, gridStr][0]
            diff = block - oldIndex

            repeat = (1000000000000 - block) // diff
            block += diff * repeat
            extraHeight += (h1-h2) * (repeat+1) + h2-checkHeight
                
            checked={}
            
        checked[operation, block%5, gridStr] = [block,len(grid)]

        block+=1

    
    res2 = len([x for x in grid if sum(x)]) - 1 + extraHeight
    print(res2)
    print(time.time()-start)