import time

with open(__file__.split('\\')[-1].replace("py","txt")) as f:
    start = time.time()
    data = f.read().split("\n")

    beaconX = []
    notBeaconX = []

    scanners = []
    beacons = []

    for d in data:
        sx,sy,bx,by = [int(x) for x in d.replace("Sensor at x=","").replace(": closest beacon is at x=",",").replace(" y=","").split(",")]
        scanners.append([sx,sy])
        beacons.append([bx,by])

        if by == 2000000: beaconX.append(bx)
        dis=abs(sx-bx)+abs(sy-by)
        size = dis-abs(sy-2000000)
        notBeaconX.extend(list(range(sx-size,sx+size+1)))
    
    print(len([x for x in list(set(notBeaconX)) if x not in beaconX]))

    res = 0
    print(res)
    print(time.time()-start)

    res2 = 0

    for d in data:
        sx,sy,bx,by = [int(x) for x in d.replace("Sensor at x=","").replace(": closest beacon is at x=",",").replace(" y=","").split(",")]

        dis=abs(sx-bx)+abs(sy-by)
        for x in range(max(sx-dis-1,0),min(sx+dis+2,4000000)):
            size=dis-abs(sx-x)+1
            p1 = [x,sy-size]

            if(sy-size < 0): p1=None
            p2 = [x,sy+size]
            if(sy+size > 4000000): p2=None
            
            foundA=p1==None
            foundB=p2==None
            for s in range(len(scanners)):
                s2=scanners[s]
                b2=beacons[s]
                if s2==[sx,sy]: continue

                dis2=abs(s2[0]-b2[0])+abs(s2[1]-b2[1])

                checksize=dis2-abs(s2[0]-x)
                if(not foundA and s2[1]-checksize <= p1[1] <= s2[1]+checksize):
                    foundA = True
                if(not foundB and s2[1]-checksize <= p2[1] <= s2[1]+checksize):
                    foundB = True

                if foundA and foundB: break

            if foundA and foundB: continue

            if not foundA and p1 is not None: 
                res2 = x*4000000+(sy-size)
                break
            if not foundB and p2 is not None:
                res2 = x*4000000+(sy+size)
                break            

        if res2: break

    print(res2)
    print(time.time()-start)