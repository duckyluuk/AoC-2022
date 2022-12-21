import time

with open(__file__.split('\\')[-1].replace("py","txt")) as f:
    start = time.time()
    data = f.read().split("\n")

    monkeys = {}
    for d in data:
        monkeys[d[:4]]=d[6:]

    #print(monkeys)
    def search(monkey):
        value=monkeys[monkey]
        if value.isnumeric():
            return int(value)
        else:
            monkeyA,operation,monkeyB = value.split(" ")
            if operation == "+": return search(monkeyA)+search(monkeyB)
            if operation == "-": return search(monkeyA)-search(monkeyB)
            if operation == "*": return search(monkeyA)*search(monkeyB)
            if operation == "/": return search(monkeyA)/search(monkeyB)


    res = search('root')
    print(res)
    print(time.time()-start)

    monkeyA,op,monkeyB = monkeys["root"].split(" ")
    
    def findEquation(monkey,equation=""):
        value = monkeys[monkey]
        if monkey=="humn": return 'x'
        if value.isnumeric(): return value
        else: 
            monkeyA,operation,monkeyB = value.split(" ")
            if monkey=='root': operation="="
            return "(" + findEquation(monkeyA) + operation + findEquation(monkeyB) + ")"


    equation = findEquation('root')
    print(equation)

    low = 0
    high = 1000000000000000

    res2 = 0
    eq1,eq2 = equation[1:-1].split("=")
    ans1 = False
    if not "x" in eq1: ans1 = eval(eq1)
    ans1 = False
    if not "x" in eq2: ans2 = eval(eq2)

    while not res2:
        guess = (low+high)//2

        # check if equation is correct
        if ans1: r1 = ans1
        else: r1 = eval(eq1.replace("x",str(guess)))

        if ans2: r2 = ans2
        else: r2 = eval(eq2.replace("x",str(guess)))

        if r1 == r2: 
            res2 = guess
            break

        # check if x should be higher or lower
        c1=eval(eq1.replace("x",str(guess+1)))
        c2=eval(eq2.replace("x",str(guess+1)))

        if abs(c1-c2) > abs(r1-r2):
            high = guess
        else:
            low = guess

    print(res2)
    print(time.time()-start)