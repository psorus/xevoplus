"""A couple of functions to tread an 1d array as a 2d one. Used by ising2d"""



def dex(i1,i2,m1,m2):
    return i1*m2+i2

def nextto8(i1,i2,m1,m2):
    p1=(i1+1)%m1
    p2=(i2+1)%m2
    s1=(i1-1+m1)%m1
    s2=(i2-1+m2)%m2
    ret=[]
    for d1 in [s1,i1,p1]:
        for d2 in [s2,i2,p2]:
            if d1==i1 and d2==i2:continue
            ret.append(dex(d1,d2,m1,m2))
    return ret
nextto=nextto8
def nextto9(i1,i2,m1,m2):
    p1=(i1+1)%m1
    p2=(i2+1)%m2
    s1=(i1-1+m1)%m1
    s2=(i2-1+m2)%m2
    ret=[]
    for d1 in [s1,i1,p1]:
        for d2 in [s2,i2,p2]:
            ret.append(dex(d1,d2,m1,m2))
    return ret

def nextto4(i1,i2,m1,m2):
    return [
            dex((i1+1)%m1,i2,m1,m2),
            dex((i1-1+m1)%m1,i2,m1,m2),
            dex(i1,(i2+1)%m2,m1,m2),
            dex(i1,(i2-1+m2)%m2,m1,m2)
            ]

def nextto5(i1,i2,m1,m2):
    return [
            dex(i1,i2,m1,m2),
            dex((i1+1)%m1,i2,m1,m2),
            dex((i1-1+m1)%m1,i2,m1,m2),
            dex(i1,(i2+1)%m2,m1,m2),
            dex(i1,(i2-1+m2)%m2,m1,m2)
            ]
def range2d(m1,m2):
    for i1 in range(m1):
        for i2 in range(m2):
            yield dex(i1,i2,m1,m2),i1,i2

def gt(q,i1,i2,m1,m2):
    assert len(q)==m1*m2

    return q[dex(i1,i2,m1,m2)]

def st(q,val,i1,i2,m1,m2):
    assert len(q)==m1*m2

    q[dex(i1,i2,m1,m2)]=val

    return q






