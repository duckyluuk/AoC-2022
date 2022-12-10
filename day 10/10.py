import time

with open(__file__.split('\\')[-1].replace("py","txt")) as f:
    start = time.time()
    data = f.read().split("\n")

    res = 0
    x=1
    tick=0

    for instruction in data:
        command = instruction.split(" ")[0]

        wait = [1,2][command=="addx"]
        for n in range(wait):
            tick+=1

            signalstrength = tick*x
            if (tick-20)%40 == 0:
                res+=signalstrength
        
        if(command=="addx"): x+=int(instruction.split(" ")[1])

    print(res)
    print(time.time()-start)


    res2=""
    x=1
    tick=0

    for instruction in data:
        command = instruction.split(" ")[0]

        wait = [1,2][command=="addx"]
        for n in range(wait):
            spritePos = [x-1,x,x+1]
            
            if tick%40 in spritePos:
                res2+="█"
            else: res2+=" "

            tick+=1

            if(tick%40 == 0): res2+="\n"
        
        if(command=="addx"): x+=int(instruction.split(" ")[1])

    print(res2)
    print(time.time()-start)