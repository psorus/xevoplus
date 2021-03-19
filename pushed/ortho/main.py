from xevo import *

from dualflip import *
from quickmut import *
from oion import oion

from mob import mob

from orthoevo import orthoevo
from morthoevo import morthoevo


import numpy as np


#job=dualflip()
#job=oion()
job=mob(oion,d=3)

#q=(meanquickmut(job,goal_mean=0.01,goal_max=0.0000001,opt=orthoevo(),maxsteps=10000,population=20))
q=(semiquickmut(job,goal=0.0000001,opt=morthoevo(),maxsteps=10000,population=20))

for zw in q:
    #print(zw.ortho()[0])
    #print(zw.ortho()[0],zw.ortho()[0]/np.pi)
    print(*zw.ortho())
    #print(*[round(zx) for zx in zw.ortho()])
    #print(zw.calcortho())
    #print(zw.strength(),zw.ortho(),[zx.calcstrength() for zx in zw.q])
    #exit()
