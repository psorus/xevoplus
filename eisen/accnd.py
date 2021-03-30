"""A couple of functions to tread an 1d array as a 2d one. Used by ising2d"""

def prod(q):
    ret=1
    for zw in q:
        ret*=zw
    return ret

def dex(i,m):
    mult=1
    ret=0
    for ii,mm in zip(i,m):
        ret+=ii*mult
        mult*=mm
    return ret


def looprange(n,modulo=1):
    i=0
    j=0
    while True:
        j+=1
        yield i
        if not j%modulo:
            i=(i+1)%n
def motiorate(offs=0,maxv=10000,modulo=1):
    i=-1
    j=0
    while True:
        j+=1
        yield (i+offs+maxv)%maxv
        if not j%modulo:
            i+=1
            if i>1:i=-1
def rangend(m):
    mult=1
    rng=[]
    for mm in m:
        rng.append(looprange(mm,mult))
        mult*=mm
    for i in range(mult):
        ac=[r.__next__() for r in rng]
        yield dex(ac,m),ac

def nextto(i,m):
    mult=1
    rng=[]
    for ii,mm in zip(i,m):
        rng.append(motiorate(offs=ii,maxv=mm,modulo=mult))
        mult*=3
    ret=[]
    for j in range(mult):
        ac=[r.__next__() for r in rng]
        #sam=[1 for acc,ii in zip(ac,i) if not acc==ii]#has elements when ac!=i
        #if len(sam)==0:continue
        
        if ac==i:continue

        ret.append(dex(ac,m))
    return ret




def gt(q,i,m):
    assert len(q)==prod(m)

    return q[dex(i,m)]

def st(q,val,i,m):
    assert len(q)==prod(m)

    q[dex(i,m)]=val

    return q



if __name__=="__main__":
    #for zw in nextto([3],[12]):
    for zw in rangend([12]):
        print(zw)


