from xevo import evo

import numpy as np
import time
import random

from simplestat import statinf


class debugtraj(evo):
    def __init__(s):
        s.initial()



    def generation(s)->None:
        for i in range(len(s.q)):
            s.q[i]=s.q[i].mutate()
        stre=[zw.strength()* (1 if zw.shallmaximize() else -1)  for zw in s.q]
        #print(statinf(stre))
        wori=np.argmin(stre)
        s.q[wori]=np.random.choice(s.q)

    

    def _copy(s):
        return debugtraj()



