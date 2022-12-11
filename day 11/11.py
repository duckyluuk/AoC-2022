import time
import numpy as np

with open(__file__.split('\\')[-1].replace("py","txt")) as f:
    start = time.time()
    data = f.read().split("\n\n")
    
    def handleItems(rounds, doDivision):
        monkeys = []
        for m in data:
            info=m.split("\n")

            monkey ={
                        "items":[int(x) for x in info[1].split(": ")[1].split(", ")],
                        "operation": "".join(info[2].split(": ")[1].split(" ")[2:]),
                        "test": int(info[3].split(": ")[1].split(" ")[2]),
                        "monkeyTo": [int(info[5].split(": ")[1].split(" ")[3]),int(info[4].split(": ")[1].split(" ")[3])],
                        "inspected": 0
                    }

            monkeys.append(monkey)
        
        # the highest possible number is all possible divisors multiplied together
        max_num= int(np.prod([m['test'] for m in monkeys]))

        for x in range(rounds):
            for m in monkeys:
                for item in m['items']:
                    item=eval(m['operation'].replace('old','item'))
                    
                    if doDivision: 
                        item=item//3
                    else: 
                        item=item%max_num

                    monkeys[m['monkeyTo'][item%m['test'] == 0]]['items'].append(item)
                    m['inspected']+=1
                m['items'] = []

        inspections=sorted(map(lambda m: m['inspected'],monkeys))
        return inspections[-1]*inspections[-2]                

    res = handleItems(20, True)
    print(res)
    print(time.time()-start)

    res2 = handleItems(10000, False)
    print(res2)
    print(time.time()-start)