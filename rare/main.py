from xevo import *


from pion import *
from bitflip import *
from gotozero import *

from trajmute import *
from trajmuteplus import *
from trivmutetraj import *
from debugtraj import *

worker=trajmute()
worker=crossevo()
#worker=trajmuteplus()
#worker=trivmutetraj()
#worker=debugtraj()

population=10
#population=200

work="pion"
#work="bitflip"
#work="gotozero"

goal=0.0

if work=="pion":
    work=pion()
    goal=1e-6
elif work=="bitflip":
    work=bitflip()
    goal=100
elif work=="gotozero":
    work=gotozero([100,100])
    #work=work.randomize()
    goal=0.1


c=erun(worker,work,population=population)

c.run(goalstrength=goal,maxsteps=1000)


win=c.getwinner()
print(win)


print(worker)

c.show_history()




