import time

with open("16.txt") as f:
    start = time.time()
    data = f.read().split("\n")

    valves={}
    maxScores={}

    for d in data:
        d=d.replace('rate=','').replace(';','').replace(",",'').split(" ")
        valves[d[1]] = {"rate":int(d[4]),"nextValves":d[9:]}
        maxScores[d[1]] = -1


    def search(routes):
        while routes:
            route=routes.pop(0)

            pos=route["pos"]

            if route["timeLeft"] <= 0: continue

            valve = valves[pos]
            for v in valve["nextValves"]:
                if maxScores[v] < route["score"]:
                    maxScores[v] = route["score"]
                    
                    routes.append({"pos":v,"timeLeft":route["timeLeft"]-1,"score":route["score"],"openValves":[*route["openValves"]]})
            
            if not pos in route["openValves"]:
                newScore = route["score"] + valve["rate"]*(route["timeLeft"]-1)
                if newScore > maxScores[pos]:
                    routes.append({"pos":pos,"timeLeft":route["timeLeft"]-1,"score":newScore,"openValves":[*route["openValves"],pos]})


    search([{"pos":"AA","timeLeft":30,"score":0,"openValves":[]}])

    res = maxScores[max(maxScores,key=maxScores.get)]
    print(res)
    print(time.time()-start)

    maxScores = {}
    for v in valves:
        for v2 in valves:
            maxScores[min(v,v2)+max(v,v2)]=-1
    

    def search2(routes):
        while routes:
            route=routes.pop(0)

            pos=route["pos"]
            pos2 = route["pos2"]

            if route["timeLeft"] <= 0: continue

            valve = valves[pos]
            valve2 = valves[pos2]

            openValves=route["openValves"]

            possible1 = []
            possible2 = []
            # generate moves for player
            for v in valve["nextValves"]:
                possible1.append([v,0,[]])
            
            if not pos in route["openValves"] and valve["rate"]:
                possible1.append([pos,valve["rate"]*(route["timeLeft"]-1),[pos]])
            # generate moves for elephant
            for v2 in valve2["nextValves"]:
                possible2.append([v2,0,[]])
            
            if not pos2 in route["openValves"] and valve2["rate"]:
                possible2.append([pos2,valve2["rate"]*(route["timeLeft"]-1),[pos2]])

            for p1 in possible1:
                for p2 in possible2:
                    newScore = route["score"]+p1[1]+p2[1]
                    check=min(p1[0],p2[0])+max(p1[0],p2[0]) # order of player and elephant dont matter
                    if newScore > maxScores[check]: # only keep checking if no better way to this point was found
                        maxScores[check] = route["score"]
                        if(p1[2] == p2[2] and p1[2] and p2[2]): continue # dont let elephant and player open same valve
                        routes.append({"pos":p1[0],"pos2":p2[0],"timeLeft":route["timeLeft"]-1,"score":newScore,"openValves":openValves+p1[2]+p2[2]})

    search2(routes=[{"pos":"AA","pos2":"AA","timeLeft":26,"score":0,"openValves":[]}])

    res2 = maxScores[max(maxScores,key=maxScores.get)]
    print(res2)
    print(time.time()-start)