from xevo.evo import evo

import numpy as np
import time
        

class ising1devo(evo):
    """1d ising optimizer with periodic boundary conditions

        shows no signs if regions (symmetry breaking) as expected, see the 2d version

    """
    
    def __init__(s,temp=1.0,garant=0.0,mergews=0.0):
        """temp: Temperature of the ising model, higher temperature->can also switch to worse result, not scale independent
           garant: difference above this->will be updated definitely. Depends on temperature
           mergews: if above zero: can add together elemts instead of replacing them"""

        s.initial()
        s.temp=temp
        s.garant=garant
        s.mergews=mergews



    def generation(s)->None:
        #s.q.sort(key=lambda x:x.ortho()[s.dex])
        nq=[zw for zw in s.q]
        lsq=len(s.q)
        sm=s.q[0].shallmaximize()
        for i in range(lsq):
            acs=s.q[i].strength()
            im=(i-1+lsq)%lsq
            ip=(i+1)%lsq
            acm=s.q[im].strength()
            acp=s.q[ip].strength()
            
            if not sm:#so now shallmaximize true
                acs*=-1
                acm*=-1
                acp*=-1
            delta=(acp+acm-2*acs)#the higher, the more probable switch
            if np.random.random()<np.exp((delta-s.garant)/s.temp):
                if acp>acm:
                    if s.mergews>0.0 and np.random.random()<s.mergews:
                        nq[i]=s.q[ip]+s.q[i]
                    else:
                        nq[i]=s.q[ip].mutate()
                else:
                    if s.mergews>0.0 and np.random.random()<s.mergews:
                        nq[i]=s.q[im]+s.q[i]
                    else:
                        nq[i]=s.q[im].mutate()

        s.q=nq


    def _copy(s):
        return ising1devo(s.wsmerge,s.dex)



