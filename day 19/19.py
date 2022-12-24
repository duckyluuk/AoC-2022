import time

with open("19.txt") as f:
    start = time.time()
    data = f.read().split("\n")

    blueprints = []

    costs = []
    for d in data:
        ore,clay,obs1,obs2,geo1,geo2=[int(x) for x in d.split(" ") if x.isnumeric()]
        cost=[]
        cost.append([ore,0,0,0])
        cost.append([clay,0,0,0])
        cost.append([obs1,obs2,0,0])
        cost.append([geo1,0,geo2,0])
        costs.append(cost)

    
    def search(costs,states,loops):
        for loop in range(loops):
            newStates = []
            for state in states:
                robots=state["robots"]
                resources=state["resources"]
                newResources = [resources[j]+robots[j] for j in range(4)]
                if resources[0] <= max(c[0] for c in costs): # if you have enough ore to afford all upgrades
                    newState = {"robots":[*robots],"resources":[*newResources]} # you have to do an upgrade
                    newStates.append(newState)

                for i in range(3,-1,-1):
                    cost = costs[i]

                    if all([resources[j]>=cost[j] for j in range(4)]):
                        if robots[i] >= max(cost[i] for cost in costs) and i<3:
                            continue # dont make more bots of a type than needed for the most expensive upgrade

                        finalRobots = [r for r in robots]
                        finalRobots[i]+=1
                        finalResources=[newResources[j]-cost[j] for j in range(4)]
                        newState = {"robots":finalRobots,"resources":finalResources}
                        newStates.append(newState)
                        if i>2: break # if you can make a geode bot then do so
            sortKey = lambda x: (x["resources"][3]+x["robots"][3]*(loops-loop))*1000 + ( # sort all states
                                 x["resources"][2]+x["robots"][2]*(loops-loop))*100  + ( # by what their final score would be
                                 x["resources"][1]+x["robots"][1]*(loops-loop))*10   + (
                                 x["resources"][0]+x["robots"][0]*(loops-loop)) 
            states = sorted(newStates, key = sortKey)[-200:] # the number might need to be higher for some but this works for my input
        return max([x["resources"][3] for x in states])
            

    res = 0
    res2 = 1
    currentState = {"robots":[1,0,0,0],"resources":[0,0,0,0]}
    for i in range(len(costs)):
        c=costs[i]
        value = search(c,[currentState],24)
        res += value * (i+1)
        #print(f"Blueprint {i+1} part 1: {value}")

    print(res)
    print(time.time()-start)

    for i in range(3):
        c=costs[i]
        value=search(c,[currentState],32)
        res2 *= value
        #print(f"Blueprint {i+1} part 2: {value}") 

    print(res2)
    print(time.time()-start)