import time

with open(__file__.split('\\')[-1].replace("py","txt")) as f:
    start = time.time()
    data = f.read().split("\n")
    convert="=-012"

    def snafu_to_dec(sna):
        dec=0
        i=1
        for n in sna:
            dec+=(convert.index(n)-2)*i
            i*=5
        return dec


    def dec_to_snafu(dec):
        if dec == 0: return ""
        return convert[(dec+2)%5]+dec_to_snafu((dec+[0,5-dec%5][dec%5>2])//5)


    total=0
    for d in data:
        num=0
        d=d[::-1]
        i=1

        dec = snafu_to_dec(d)
        total+=dec

    
    res = dec_to_snafu(total)[::-1]
    print(res)
    print(time.time()-start)

    
    res2 = 0
    print(res2)
    print(time.time()-start)