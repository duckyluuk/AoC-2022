import time

with open(__file__.split('\\')[-1].replace("py","txt")) as f:
    start = time.time()
    data = f.read().split("\n")

    res = 0
    for d in data:
        a,b=[[int(y) for y in x.split("-")] for x in d.split(",")]
        if (a[0]<=b[0] and b[1]<=a[1]) or (b[0]<=a[0] and a[1]<=b[1]):
            res+=1

    print(res)
    print(time.time()-start)

    res2 = 0
    for d in data:
        a,b=[[int(y) for y in x.split("-")] for x in d.split(",")]
        if (b[0]<=a[1] and b[1]>=a[1]) or (a[0]<=b[1] and a[1]>=b[1]):
            res2+=1

    print(res2)
    print(time.time()-start)
