import time
from functools import cmp_to_key

with open(__file__.split('\\')[-1].replace("py","txt")) as f:
    start = time.time()
    data = f.read().split("\n\n")
    pairs = [[eval(l) for l in pair.splitlines()]for pair in data]

    res = 0

    def compare(left,right):
        if type(left) == int and type(right) == int:
            return right - left

        if type(left) == list and type(right) == list:
            for x in range(min(len(left), len(right))):
                comp = compare(left[x],right[x])
                if comp: return comp
            return len(right)-len(left)

        if type(left) == int and type(right) == list:
            return compare([left],right)
        if type(left) == list and type(right) == int:
            return compare(left,[right])

    for i,[left,right] in enumerate(pairs,1):
        if(compare(left,right) > 0):
            res+=i

    print(res)
    print(time.time()-start)

    packetList = [item for pair in pairs for item in pair]
    packetList.append([[2]])
    packetList.append([[6]])

    l=sorted(packetList, key=cmp_to_key(compare),reverse=True)
    
    res2 = (l.index([[2]])+1)*(l.index([[6]])+1)
    print(res2)
    print(time.time()-start)