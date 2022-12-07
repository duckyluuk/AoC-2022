import time

with open(__file__.split('\\')[-1].replace("py","txt")) as f:
    start = time.time()
    data = f.read().split("\n")

    res = 0
    filesystem = {}
    path = "/"
    for c in data:
        if(c[0] == "$"):
            command = c.split(" ")[1]
            if(command == "cd"):
                location = c.split(" ")[2]
                if(location == "/"):
                    path = "/"
                elif(location == ".."):
                    path = "/".join(path.split("/")[:-1])
                    if(len(path) == 0): path = "/"
                elif len(path)>1:
                    path+="/"+location
                else: 
                    path+=location

            if(command == 'ls'):
                filesystem[path] = {'folders':[],'files':[]}
        else:
            size,name = c.split(" ")
            if(size == "dir"):
                filesystem[path]['folders'].append(path+['','/'][len(path)>1]+name)
            else:
                filesystem[path]['files'].append(int(size))


    def getSize(dir):
        size = sum(filesystem[dir]['files'])
        for f in filesystem[dir]['folders']:
            size+=getSize(f)

        return size
    
    for dir in filesystem.keys():
        size = getSize(dir)
        if(size <= 100000):
            res+=size

    print(res)
    print(time.time()-start)

    res2=99999999
    neededSize = 30000000-(70000000-getSize("/"))
    for dir in filesystem.keys():
        size = getSize(dir)
        if(size >= neededSize):
            res2=min(res2,size)

    print(res2)
    print(time.time()-start)