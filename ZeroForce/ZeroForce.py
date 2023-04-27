import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import collections
import itertools
from itertools import combinations
import copy 
import math
import matplotlib.animation as animation
#%matplotlib notebook

def printGraph1(G):
  pos=nx.get_node_attributes(G,'pos')
  nx.draw(G,pos)


def printGraph(G, ax, blue = []):
  color = []
  pos=nx.get_node_attributes(G,'pos')
  for node in G.nodes():
    if not node in blue:
      color.append("red")
    else:
      color.append("blue")
  nx.draw(G,pos,node_color=color,ax=ax)
  return(ax,)


def Snark(n):
  G=nx.Graph()
  deg = math.radians(18)
  for i in range(5):
    G.add_node((0,i),pos=(1*math.cos(deg),1*math.sin(deg)))
    G.add_node((1,i),pos=(2*math.cos(deg),2*math.sin(deg)))
    G.add_edge((0,i),(1,i))
    deg += math.radians(72)
  for i in range(5):
    G.add_edge((0,i),(0,(i+2)%5))
    G.add_edge((1,i),(1,(i+1)%5))
  return(G)

def AddEdgeIf(G,cN,uN):
  """"Add edge it it is possible
  G =  Graph
  cN  = Certain node
  uN = Uncertan node"""
  if uN in G.nodes() and not (cN,uN) in G.edges():
    G.add_edge(cN,uN)

def FiveFlower():
  G=nx.Graph()
  deg = math.radians(18)
  for i in range(5):
    G.add_node((0,i),pos=(1*math.cos(deg),1*math.sin(deg)))
    G.add_node((1,i),pos=(3*math.cos(deg),3*math.sin(deg)))
    G.add_edge((0,i),(1,i))
    deg += math.radians(72)
  deg = math.radians(18)
  for i in range(5):
    G.add_edge((0,i),(0,(i+1)%5))
    G.add_node((2,2*i),pos=(3*math.cos(deg-math.radians(18)),3*math.sin(deg-math.radians(18))))
    G.add_node((2,2*i+1),pos=(3*math.cos(deg+math.radians(18)),3*math.sin(deg+math.radians(18))))
    G.add_edge((1,i),(2,2*i+1))
    G.add_edge((1,i),(2,2*i))
    
    AddEdgeIf(G,(2,2*i+1),(2,(2*i+2)%10))
    AddEdgeIf(G,(2,2*i),(2,(2*i-1)))
    AddEdgeIf(G,(2,2*i),(2,((2*(i+1)+1))%10))
    AddEdgeIf(G,(2,2*i+1),(2,(2*(i-1))))
    deg += math.radians(72)
  return(G)



def Path(n):
  G=nx.Graph()
  G.add_node(0,pos=(0,0))
  for i in range(n-1):
    G.add_node(i+1,pos=(i+1,0))
    G.add_edge(i,i+1)
  return(G)

def Cycle(n):
  G=nx.Graph()
  deg = 0
  deg_add = math.pi*2/n
  G.add_node(0,pos=(1*math.cos(deg),1*math.sin(deg)))
  for i in range(n-1):
    deg += deg_add
    G.add_node(i+1,pos=(1*math.cos(deg),1*math.sin(deg)))
    G.add_edge(i,i+1)
  G.add_edge(0,i+1)
  return(G)

def FullyConnected1(n):
  G=nx.Graph()
  G.add_node((0,0),pos=(0,0))
  G.add_node((1,0),pos=(0,1))
  G.add_edge((0,0),(1,0))
  for i in range(n-1):
    G.add_node((0,i+1),pos=(i+1,0))
    G.add_node((1,i+1),pos=(i+1,1))
    G.add_edge((0,i+1),(1,i+1))
    for j in range(i+1):
      G.add_edge((0,i+1),(0,j))
      G.add_edge((1,i+1),(0,j))
      G.add_edge((0,i+1),(1,j))
      G.add_edge((1,i+1),(1,j))
  return(G)

def BiGraph(n):
  G=nx.Graph()
  G.add_node((0,0),pos=(0,0))
  G.add_node((1,0),pos=(0,1))
  G.add_edge((0,0),(1,0))
  for i in range(n-1):
    G.add_node((0,i+1),pos=(i+1,0))
    G.add_node((1,i+1),pos=(i+1,1))
    G.add_edge((0,i+1),(1,i+1))
    for j in range(i+1):
      G.add_edge((1,i+1),(0,j))
      G.add_edge((0,i+1),(1,j))
  return(G)


def Pyramid(n):
  G=nx.Graph()
  G.add_node((0,0),pos=(0,0))
  for i in range(n-1):
    G.add_node((i+1,0),pos=(-i-1,0))
    G.add_edge((i+1,0),(i,0))
    for j in range(i+1):
      G.add_node((i+1,j+1),pos=(-i-1,j+1))
      G.add_edge((i+1,j+1),(i,j))
      G.add_edge((i+1,j+1),(i+1,j))
  return(G)

      


"""def FullyConnected(n):
  G=nx.Graph()
  rowsN = math.floor(math.log2(n))
  colsN = math.ceil(n/rowsN)
  i = 0
  r = 0
  while i<n:
    G.add_node(i,pos=(i+1,0))


    i+=1"""

def Forcing(G,blue):
  addTo = []
  for node in blue:
    newblue = []
    neighbors = G.neighbors(node)
    for n in neighbors:
      if not n in blue:
        newblue.append(n)
    if len(newblue) == 1 and not newblue[0] in addTo:
      addTo.append(newblue[0])
  blue = list(blue)

  return(blue + addTo)


def ZeroForcing1(G,n, AnimationName = ""):
  Frames = False
  if AnimationName != "":
    Frames = True
  if Frames:
    frames = []
    fig= plt.figure()
  combs= list(combinations(G.nodes(),n))
  for comb in combs:
    blue = comb
    while True:
      if Frames:
        ax=fig.add_subplot()
        frames.append(printGraph(G,ax, blue= blue))
      newblue = Forcing(G,blue)
      if len(newblue) == len(G.nodes()):
        if Frames:
          ax=fig.add_subplot()
          frames.append(printGraph(G,ax, blue= newblue))
          ani = animation.ArtistAnimation(fig, frames, interval = 500)
          ani.save(AnimationName + ".gif")
          #plt.show()
        return(comb)
      if len(newblue) == len(blue):
        break
      else:
        blue = newblue

  if Frames:
    ani = animation.ArtistAnimation(fig, frames)
    ani.save(AnimationName + ".gif")
  return(False)


def ZeroForcing(G, AnimationName = ""):
  n = min(G.degree(G.nodes()))[1]
  N = len(G.nodes())
  while n < N-1:
    start = ZeroForcing1(G,n,AnimationName = AnimationName)
    if start:
      return(start)
    n +=1
  return(N-1)



def AnimationForce(G, blue, AnimationName):
    Frames = True
    if Frames:
        frames = []
        fig= plt.figure()
    while True:
        if Frames:
            ax=fig.add_subplot()
            frames.append(printGraph(G,ax, blue= blue))
        newblue = Forcing(G,blue)
        if len(newblue) == len(G.nodes()):
            if Frames:
                ax=fig.add_subplot()
                frames.append(printGraph(G,ax, blue= newblue))
            break
        if len(newblue) == len(blue):
            break
        else:
            blue = newblue

    if Frames:
        ani = animation.ArtistAnimation(fig, frames, interval = 500)
        ani.save(AnimationName + ".gif")
    return(False)



G = FiveFlower()
#print(ZeroForcing(G,AnimationName = ""))
print(ZeroForcing(G,AnimationName = "5FlowerSearch"))
#AnimationForce(G, ((0, 0), (1, 0), (0, 1), (1, 1), (1, 2), (2, 0), (2, 2)), "5Flower")

"""G = Cycle(12)
G.add_node(12,pos = (0,2))
G.add_edge(3,12)
G.add_node(13,pos = (-0.5,-2))
G.add_edge(8,13)
G.add_node(14,pos = (0.5,-2))
G.add_edge(9,14)
AnimationForce(G, (2,12), "OnlyTrueCyleWith3in31")
print(ZeroForcing(G,AnimationName = ""))"""