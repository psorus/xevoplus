from xevo import evo

import numpy as np
import time
import random

class trajmute(evo):
  """given n ways, replace the worst by the best, mutate the rest """
  
  def initial(s):
    evo.initial(s)
    s.q=[]
  def populate(s,person,n=10)->None:
    s.n=n
    s.q=[person.copy() for i in range(n)]#.randomize()
  
  def winner(s)->int:
    if s.shallmaximize():
      return np.argmax([zw.strength() for zw in s.q])
    else:
      return np.argmax([-zw.strength() for zw in s.q])
  def topn(s,n=3)->"[int]":
    if s.shallmaximize():
      return np.argsort([-zw.strength() for zw in s.q])[:n]
    else:
      return np.argsort([zw.strength() for zw in s.q])[:n]
  def average(s)->"float,float":
    stre=[zw.strength() for zw in s.q]
    return np.mean(stre),np.std(stre)
  
  def __getitem__(s,key):
    return s.q[key]
  def __set_item__(s,key,obj):
    s.q[key]=obj
  
  def copy(s):
    ret=s._copy()
    ret.n=s.n
    ret.q=[zw.copy() for zw in s.q]
    return ret
  
  def __init__(s):
    s.initial()



  def generation(s)->None:
    os=s.q.strength()
    if random.random()<0.5:
      n=s.q.randomize()
    else:
      n=s.q.mutate()
    ns=n.strength()
    if ns<=os:
      s.q=n
      if hasattr(s.q,"getsave"):s.q.getsave()("data/bestobj.txt")
    
    


  def _copy(s):
    return trajmute()



