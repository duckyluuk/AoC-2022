import time

with open(__file__.split('\\')[-1].replace("py","txt")) as f:
    data=f.read()
    start = time.time()
    
    def solve(rounds, multiplier):
        numbers = [int(x)*multiplier for x in data.split("\n")]
        indexes = list(range(len(numbers)))
        for x in range(rounds):
            for index, value in enumerate(numbers):
                indexLocation = 0
                for i in indexes:
                    if indexes[i] == index:
                        indexLocation = i
                        break
                indexes.pop(indexLocation)
                indexes.insert((indexLocation+value) % (len(numbers)-1), index)

        numbers = [numbers[i] for i in indexes]
        
        zeroIndex = 0
        for i in range(len(numbers)):
            if numbers[i]==0:
                zeroIndex=i
                break
        return sum([numbers[(zeroIndex+x)%len(numbers)] for x in [1000,2000,3000]])
        

    res = solve(1,1)
    print(res)
    print(time.time()-start)

    
    res2 = solve(10,811589153)
    print(res2)
    print(time.time()-start)