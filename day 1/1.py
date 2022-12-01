import time

with open(__file__.split('\\')[-1].replace("py","txt")) as f:
    start = time.time()
    data = f.read().split("\n\n")

    totals = sorted([sum([int(x) for x in d.split("\n") if x]) for d in data])
    res=totals[-1]
    print(res)
    print(time.time()-start)

    
    res2 = sum(totals[-3:])
    print(res2)
    print(time.time()-start)