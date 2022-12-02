import time

with open("2.txt") as f:
    start = time.time()
    data = f.read().split("\n")

    res = 0

    for d in data:
        opponent,self = d.split(" ")
        opponent,self = int(opponent,36)-9,int(self,36)-32
        res+=self
        if(opponent == self): res+=3
        elif((self - opponent in [1,-2])): res+=6

    print(res)
    print(time.time()-start)

    
    res2 = 0

    for d in data:
        opponent, result = d.split(" ")
        opponent, result = int(opponent,36)-10,int(result,36)-34
        res2+=3*(result+1)
        res+=[1,2,3][(opponent+result)%3]

    print(res2)
    print(time.time()-start)