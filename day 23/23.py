import time

with open(__file__.split('\\')[-1].replace("py","txt")) as f:
    start = time.time()
    data = [list(d) for d in f.read().split("\n")]
    elfLocations = []
    elfCount = 0

    for y,r in enumerate(data):
        for x,s in enumerate(r):
            if s=="#":
                elfLocations.append([x,y])  
                elfCount += 1
    print(elfCount)      
    rounds = 10
    dir = [[[-1,-1],[0,-1],[1,-1]],[[-1,1],[0,1],[1,1]],[[-1,-1],[-1,0],[-1,1]],[[1,-1],[1,0],[1,1]]]
    checkElfLocations = []
    num=0
    while elfLocations != checkElfLocations:
        #print(num)
        checkElfLocations = [x for x in elfLocations]
        newElfLocations = []

        while elfLocations:
            elf = elfLocations.pop()
            count = 0
            for d in [[-1,-1],[0,-1],[1,-1],
                      [-1,0],        [1,0],
                      [-1,1], [0,1], [1,1]]:
                if [elf[0]+d[0],elf[1]+d[1]] in checkElfLocations:
                    count += 1
                    break
            #print(count)
            if count == 0:
                newElfLocations.append([[elf[0],elf[1]],[elf[0],elf[1]]])
                continue
            for d in dir:
                count = 0
                for p in d:
                    if [elf[0]+p[0],elf[1]+p[1]] in checkElfLocations:
                        count += 1     
                        break
                #print(elf,count,[elf[0]+d[1][0],elf[1]+d[1][1]],d)           
                if count == 0:
                    newElfLocations.append([[elf[0]+d[1][0],elf[1]+d[1][1]],[elf[0],elf[1]]])
                    break
            else:
                newElfLocations.append([[elf[0],elf[1]],[elf[0],elf[1]]])
            #print(newElfLocations[-1])
        print("middle")

        while newElfLocations:
            elf = newElfLocations.pop()
            if elf[0] in [e[0] for e in newElfLocations]:
                for i,e in enumerate(newElfLocations):
                    if e[0] == elf[0]:
                        elfLocations.append(e[1])
                        newElfLocations.pop(i)
                        break
                #newElfLocations = [e for e in newElfLocations if e[0] != elf[0]]
                elfLocations.append(elf[1])
            else: elfLocations.append(elf[0])
        dir.append(dir.pop(0))
        num+=1
        
        
        if num==10:
            minX = min(e[0] for e in elfLocations)
            maxX = max(e[0] for e in elfLocations)

            minY = min(e[1] for e in elfLocations)
            maxY = max(e[1] for e in elfLocations)

            size = (maxX-minX+1) * (maxY-minY+1)


            res = size-elfCount
            print(res)
            print(time.time()-start)

        print("end")



    
    res2 = num
    print(res2)
    print(time.time()-start)