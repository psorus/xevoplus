import numpy as np
import sys

temp=float(sys.argv[1])

f=np.load(f"var/{temp}.npz")

mean=f["mean"]
std=f["std"]
q=f["q"]
s=f["s"]

from plt import *

def doone(q,nam):
    print("")
    print("")
    print(nam)
    plt.plot(q,label="data")
    x=np.arange(len(q))
    m,b=np.polyfit(x,q,1)
    ft=b+m*x
    plt.plot(ft,alpha=0.5,color="black",label="fit")
    plt.yscale("log")
    plt.legend()
    plt.show()
    print("std",np.std(q))
    print("m/100k",m*100000)


doone(mean,"mean")
doone(std,"std")
doone(q,"q")
doone(s,"s")



