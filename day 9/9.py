import time

with open(__file__.split('\\')[-1].replace("py","txt")) as f:
    start = time.time()
    data = f.read().split("\n")

    visitedPositions = ["[0,0]"]
    tx=ty=hx=hy=0

    def updateTail():
        global tx,ty,hx,hy

        dx=hx-tx
        dy=hy-ty

        if dx==0 and abs(dy)>1:
            ty+=[-1,1][dy>0]
        elif dy==0 and abs(dx)>1:
            tx+=[-1,1][dx>0]

        elif abs(dx)+abs(dy)>2:
            if dx>0:
                tx+=1
            if dx<0:
                tx-=1
            if dy>0:
                ty+=1
            if dy<0:
                ty-=1

        visitedPositions.append(str([tx,ty]))


    for d in data:
        direction, amount = d.split(" ")
        amount=int(amount)

        if direction=="U":
            for i in range(amount):
                hy+=1
                updateTail()
        if direction=="D": 
            for i in range(amount):
                hy-=1
                updateTail()
        if direction=="R":
            for i in range(amount):
                hx+=1
                updateTail()
        if direction=="L": 
            for i in range(amount):
                hx-=1
                updateTail()

    res = len(set(visitedPositions))
    print(res)
    print(time.time()-start)


    positions = [[0,0] for i in range(10)]
    visitedPositions = []
    def updateRope():
        global positions
        for p in range(len(positions)-1):
            dx=positions[p][0]-positions[p+1][0]
            dy=positions[p][1]-positions[p+1][1]

            if dx==0 and abs(dy)>1:
                positions[p+1][1]+=[-1,1][dy>0]
            elif dy==0 and abs(dx)>1:
                positions[p+1][0]+=[-1,1][dx>0]

            elif abs(dx)+abs(dy)>2:
                if dx>0 and dy>0:
                    positions[p+1][0]+=1
                    positions[p+1][1]+=1
                if dx>0 and dy<0:
                    positions[p+1][0]+=1
                    positions[p+1][1]-=1
                if dx<0 and dy<0:
                    positions[p+1][0]-=1
                    positions[p+1][1]-=1
                if dx<0 and dy>0:
                    positions[p+1][0]-=1
                    positions[p+1][1]+=1
        
        visitedPositions.append(str(positions[9]))


    for d in data:
        direction, amount = d.split(" ")
        amount=int(amount)

        if direction=="U":
            for i in range(amount):
                positions[0][1]+=1
                updateRope()
        if direction=="D": 
            for i in range(amount):
                positions[0][1]-=1
                updateRope()
        if direction=="R":
            for i in range(amount):
                positions[0][0]+=1
                updateRope()
        if direction=="L": 
            for i in range(amount):
                positions[0][0]-=1
                updateRope()

    
    res2 = len(set(visitedPositions))
    print(res2)
    print(time.time()-start)