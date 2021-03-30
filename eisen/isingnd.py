from xevo.evo import evo

import numpy as np
import time

from accnd import st,gt,dex,nextto,rangend


from numpy import mean,argmax


class isingndevo(evo):
    """n dimensional ising optimizer with periodic boundary conditions


    """
    
    def __init__(s,m=None,temp=1.0,garant=0.0,mergews=0.0,mean_func="mean",close="o"):
        """m: array of the sizes of the fields. Have to match the population size. Standart values multiply to standart values for quickmut( 2*2*5=20, not optimal!)
           temp: Temperature of the ising model, higher temperature->can also switch to worse result, not scale independent
           garant: difference above this->will be updated definitely. Depends on temperature
           mergews: if above zero: can add together elemts instead of replacing them (not implemented atm)
           mean_func: average function in the ising loss (average(neighbourhood)-mine), understands mean,max,min or callable
           close: type of neighbourhood, understands o (8 around in 2d) or callable

           """

        s.initial()
        if m is None:m=[2,2,5]
        s.m=m
        s.temp=temp
        s.garant=garant
        s.mergews=mergews

        if mean_func=="mean":mean_func=mean
        if mean_func=="max":mean_func=max
        if mean_func=="min":mean_func=min

        if close=="o":close=nextto
        #if close=="c":close=nextto4
        #if close=="9":close=nextto9
        #if close=="+":close=nextto5

        s.mean_func=mean_func
        s.close=close



    def generation(s)->None:
        #s.q.sort(key=lambda x:x.ortho()[s.dex])
        nq=[zw for zw in s.q]
        lsq=len(s.q)
        sm=s.q[0].shallmaximize()
        for i,ii in rangend(s.m):
            acs=s.q[i].strength()
            ic=s.close(ii,s.m)
            acc=[s.q[j].strength() for j in ic]
            
            if not sm:#so now shallmaximize true
                acs*=-1
                acc=[zw*-1 for zw in acc]
            delta=(s.mean_func(acc)-acs)#the higher, the more probable switch (better: the more energy loss, the less likely take worse event)
            if np.random.random()<np.exp((delta-s.garant)/s.temp):
                dex=argmax(acc)
                if acc[dex]<acs or ic[dex]==i:
                    nq[i]=s.q[i].copy()
                    continue
                if s.mergews>0.0 and np.random.random()<s.mergews:
                    nq[i]=s.q[ic[dex]]+s.q[i]
                else:
                    nq[i]=s.q[ic[dex]].mutate()

        s.q=nq


    def _copy(s):
        return isingndevo(m=[zw for zw in s.m],temp=s.temp,garant=s.garant,mergews=s.mergews,mean_func=s.mean_func,close=s.close)

    def to_array(s,odex=0):
        ret=np.zeros(s.m)
        for i,ii in rangend(s.m):
            ret.__setitem__(*ii,s.q[i].ortho()[odex])
        return ret




