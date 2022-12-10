import time

with open("9.txt") as f:
    start = time.time()
    data = f.read().split("\n")

    def moveRope(size):
        positions = [[0,0] for i in range(size)]
        visitedPositions = []
        def updateRope():
            for p in range(len(positions)-1):
                dx=positions[p][0]-positions[p+1][0]
                dy=positions[p][1]-positions[p+1][1]

                if dx==0 and abs(dy)>1:
                    positions[p+1][1]+=[-1,1][dy>0]
                elif dy==0 and abs(dx)>1:
                    positions[p+1][0]+=[-1,1][dx>0]

                elif abs(dx)+abs(dy)>2:
                    positions[p+1][1]+=[-1,1][dy>0]
                    positions[p+1][0]+=[-1,1][dx>0]
            
            visitedPositions.append(str(positions[len(positions)-1]))

        for d in data:
            direction, amount = d.split(" ")

            if direction=="U":
                move=[0,1]
            if direction=="D": 
                move=[0,-1]
            if direction=="R":
                move=[1,0]
            if direction=="L": 
                move=[-1,0]
            for i in range(int(amount)):
                positions[0][0]+=move[0]
                positions[0][1]+=move[1]
                updateRope()
        
        return len(set(visitedPositions))

    res=moveRope(2)
    print(res)
    print(time.time()-start)

    res2=moveRope(10)
    print(res2)
    print(time.time()-start)