import time

with open(__file__.split('\\')[-1].replace("py","txt")) as f:
    start = time.time()
    data = f.read().split("\n")

    res = 0

    for d in data:
        opponent,self = d.split(" ")
        if(opponent == "A" and self == "X"): res+=3+1
        if(opponent == "A" and self == "Y"): res+=6+2
        if(opponent == "A" and self == "Z"): res+=0+3

        if(opponent == "B" and self == "X"): res+=0+1
        if(opponent == "B" and self == "Y"): res+=3+2
        if(opponent == "B" and self == "Z"): res+=6+3

        if(opponent == "C" and self == "X"): res+=6+1
        if(opponent == "C" and self == "Y"): res+=0+2
        if(opponent == "C" and self == "Z"): res+=3+3

    print(res)
    print(time.time()-start)

    
    res2 = 0

    for d in data:
        opponent, result = d.split(" ")
        if(opponent == "A" and result == "X"): res2+=0+3
        if(opponent == "A" and result == "Y"): res2+=3+1
        if(opponent == "A" and result == "Z"): res2+=6+2

        if(opponent == "B" and result == "X"): res2+=0+1
        if(opponent == "B" and result == "Y"): res2+=3+2
        if(opponent == "B" and result == "Z"): res2+=6+3

        if(opponent == "C" and result == "X"): res2+=0+2
        if(opponent == "C" and result == "Y"): res2+=3+3
        if(opponent == "C" and result == "Z"): res2+=6+1

    print(res2)
    print(time.time()-start)