from xevo.evo import evo

import numpy as np
import time

from acc2d import st,gt,dex,nextto,range2d
from acc2d import nextto5,nextto4,nextto9,nextto8


from numpy import mean,argmax


class ising2devo(evo):
    """2d ising optimizer with periodic boundary conditions


    """
    
    def __init__(s,m1=4,m2=5,temp=1.0,garant=0.0,mergews=0.0,mean_func="mean",close="o"):
        """m1, m2: sizes of the fields. Have to match the population size. Standart values multiply to standart values for quickmut
           temp: Temperature of the ising model, higher temperature->can also switch to worse result, not scale independent
           garant: difference above this->will be updated definitely. Depends on temperature
           mergews: if above zero: can add together elemts instead of replacing them (not implemented atm)
           mean_func: average function in the ising loss (average(neighbourhood)-mine), understands mean,max,min or callable
           close: type of neighbourhood, understands o (8 around) c (checkerboard, 4 around), 9 (o+ self), + (4+self) or callable

           """

        s.initial()
        s.m1=m1
        s.m2=m2
        s.temp=temp
        s.garant=garant
        s.mergews=mergews

        if mean_func=="mean":mean_func=mean
        if mean_func=="max":mean_func=max
        if mean_func=="min":mean_func=min

        if close=="o":close=nextto8
        if close=="c":close=nextto4
        if close=="9":close=nextto9
        if close=="+":close=nextto5

        s.mean_func=mean_func
        s.close=close



    def generation(s)->None:
        #s.q.sort(key=lambda x:x.ortho()[s.dex])
        nq=[zw for zw in s.q]
        lsq=len(s.q)
        sm=s.q[0].shallmaximize()
        for i,i1,i2 in range2d(s.m1,s.m2):
            acs=s.q[i].strength()
            ic=s.close(i1,i2,s.m1,s.m2)
            acc=[s.q[ii].strength() for ii in ic]
            
            if not sm:#so now shallmaximize true
                acs*=-1
                acc=[zw*-1 for zw in acc]
            delta=(s.mean_func(acc)-acs)#the higher, the more probable switch
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
        return ising2devo(s,m1=s.m1,m2=s.m2,temp=s.temp,garant=s.garant,mergews=s.mergews,mean_func=s.mean_func,close=s.close)


    def to_array(s,odex=0):
        ret=np.zeros((s.m1,s.m2))
        for i1 in range(s.m1):
            for i2 in range(s.m2):
                ret[i1,i2]=s.q[dex(i1,i2,s.m1,s.m2)].ortho()[odex]
        return ret




