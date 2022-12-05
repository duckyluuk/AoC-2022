import time

with open(__file__.split('\\')[-1].replace("py","txt")) as f:
    start = time.time()
    begin,moves = f.read().split("\n\n")

    data1 = [[] for x in range(9)]
    data2 = [[] for x in range(9)]
    for j in range(len(begin.split("\n"))-1):
        line=begin.split("\n")[j]
        for i in range(1,len(line),4):
            if(line[i]!=" "):
                print(line[i])
                data1[i//4+1-1].append(line[i])
                data2[i//4+1-1].append(line[i])

    for d in range(len(data1)):
        data1[d] = data1[d][::-1]
        data2[d] = data1[d][::-1]
    
    for move in moves.split("\n"):
        amount=int(move.split(" ")[1])
        original=int(move.split(" ")[3])-1
        goal=int(move.split(" ")[5])-1

        for i in range(amount):
            c=data1[original].pop()
            data1[goal].append(c)

        data2[original],c=data2[original][:-amount],data2[original][-amount:]
        data2[goal]+=c
    
    res = ""
    for d in data1:
        res+=d[-1]

    print(res)
    print(time.time()-start)     

    res2 = ""
    for d in data2:
        res2+=d[-1]
    
    print(res2)
    print(time.time()-start)