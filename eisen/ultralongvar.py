



from xevo import quickmut,oobj,crossevo,semiquickmut
from xevo.objects import oion

import numpy as np

from ising1d import ising1devo
from ising2d import ising2devo

#from plt import *
import matplotlib.pyplot as plt

from time import sleep

from acc2d import range2d

temp=1000

import sys
if len(sys.argv)>1:
    temp=float(sys.argv[1])


variances=[]
strengths=[]
means=[]
stds=[]


class varlog(ising2devo):
    def acvar(s):
        q=s.to_array()
        q/=np.pi
        q=q.flatten().astype("int").tolist()
        #print(set(q))
        return len(set(q))
    def generation(s):
        ising2devo.generation(s)
        if s.i<100:return
        global variances
        global strengths
        global temp
        global means
        global stds
        variances.append(s.acvar())
        strengths.append(s.getwinner().strength())
        mean,std=s.average()
        means.append(mean)
        stds.append(std)
        if not ((s.i%1000) or s.i==0):
            print("saving")
            np.savez_compressed("var/"+str(temp),q=variances,t=temp,s=strengths,mean=means,std=stds)
        print(variances[-1])

obj=oion()


m1=25
m2=25


#opt=crossevo()
#opt=ising1devo(temp=1.0)
#opt=showii(temp=0.1,m1=m1,m2=m2,mergews=0.3)
opt=varlog(temp=float(temp),m1=m1,m2=m2,close="o")



#q=quickmut(obj,opt=opt,population=m1*m2)
q=semiquickmut(obj,opt=opt,population=m1*m2,maxsteps=1000000)

print(variances)
print(set(variances))


