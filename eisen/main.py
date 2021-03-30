



from xevo import quickmut,oobj,crossevo,semiquickmut
from xevo.objects import oion

import numpy as np

from ising1d import ising1devo
from ising2d import ising2devo
from isingnd import isingndevo

#from plt import *
import matplotlib.pyplot as plt

from time import sleep

from acc2d import range2d
from accnd import prod,rangend


class showii(ising2devo):
    def generation(s):
        ising2devo.generation(s)
        #try:
        for iiii in range(1):
            if s.i%int(np.sqrt(s.i+1)) and s.i!=999:continue
            if np.random.random()<0.7 and s.i!=999:continue
            #if s.i<999:continue
            dat=s.to_array()
            dat=dat.astype("float")
            dat-=np.min(dat)
            dat/=np.max(dat)

            plt.imshow(dat)
            plt.title(str(s.i))
            plt.show()
            plt.close()
        #except:
        #    print(s.to_array())
        #sleep(1)
        #print(s.to_array())


obj=oion()


m1=50
m2=50

m=[10,10,10,10]


#opt=crossevo()
#opt=ising1devo(temp=1.0)
#opt=showii(temp=0.1,m1=m1,m2=m2,mergews=0.3)
#opt=showii(temp=10.0,m1=m1,m2=m2,close="o")
opt=isingndevo(temp=10.0,m=m)


#q=quickmut(obj,opt=opt,population=m1*m2)
q=semiquickmut(obj,opt=opt,population=prod(m))


##useful for 1d
#ts=([[zw.ortho()[0],zw.strength()] for zw in q])
#plt.imshow([[zw[0] for zw in ts]])
#plt.show()
#plt.imshow([[zw[1] for zw in ts]])
#plt.show()


##useful for 2d
#rel=np.zeros((m1,m2))
#for i,i1,i2 in range2d(m1,m2):
#    rel[i1,i2]=np.log(q[i].strength()+0.0001)
#plt.imshow(rel)
#plt.show()



print(q)
print(q.q/np.pi)



