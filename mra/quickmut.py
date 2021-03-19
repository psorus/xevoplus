from xevo import crossevo,erun




def quickmut(obj,population=20,goal=0.0,maxsteps=1000,show=True):

    c=erun(crossevo(),obj,population=population,show=show)
    c.run(goalstrength=goal,maxsteps=maxsteps)
    return c.getwinner()



