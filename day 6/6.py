import time

with open(__file__.split('\\')[-1].replace("py","txt")) as f:
    start = time.time()
    data = f.read()

    for i in range(4,len(data)):
        if(len(set(data[i-4:i]))==4): print(i); break

    print(time.time()-start)
    

    for i in range(14,len(data)):
        if(len(set(data[i-14:i]))==14): print(i); break
    
    print(time.time()-start)