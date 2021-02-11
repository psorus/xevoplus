from xevo import *
import matplotlib.pyplot as plt
import numpy as np

from pion import *
from bitflip import *
from gotozero import *

from trajmute import *
from trivmutetraj import *




def calcle(q):
    work=gotozero(q)
    worker=trivmutetraj()
    c=erun(worker,work,show=False)
    
    c.run(goalstrength=0.1,maxsteps=1000)
    
    return worker.forget#2**(-worker.forget)


def fordis(n):
    return np.mean([calcle([n,n]) for i in range(10)])


x=[]
y=[]
for i in range(3,40):
    x.append(i*np.sqrt(2))
    y.append(fordis(i))
    print("did",i)

plt.plot(x,y)
plt.show()





