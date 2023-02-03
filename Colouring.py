from copy import deepcopy
def m_colouring(W,i,vcolour,n,colours):
    if promising(W,i,vcolour,n):
        if i == n-1:
            print(vcolour)
        else:
            for colour in colours:
                vcolour[i+1] = colour
                m_colouring(W,i+1,vcolour,n,colours)

def promising(W,i,vcolour,n):
    for j in range(i):
        if W[i][j]:
            if vcolour[i] == vcolour[j]:
                return(False)
    return(True)


def WtoComp(W):
    oupt = []
    k = 0
    for i in W:
        count = 0
        for j in i:
            if j:
                count +=1
        oupt.append((k,count))
        k+=1
    return(oupt)
def isGoal(vcolour):
    for i in vcolour:
        if not i:
            return(False)
    return(True)

def promising2(W,i,vcolour):
    for j in range(len(vcolour)):
        if W[i][j]:
            if vcolour[i] == vcolour[j]:
                return(False)
    return(True)


def m_colouring_heuristic(W,colours):
    """Make a coloring algorithum that runs through each color and colours as many nodes as it can that colour starting with the most complex(most attached) ones"""
    n = len(W)
    vcolour = [0]*n
    comps = WtoComp(W)
    comps.sort(key = lambda x: x[1], reverse=True)
    for colour in colours:
        new_comps = deepcopy(comps)
        for i in comps:
            vcolour[i[0]] = colour
            #print(vcolour)
            #print(comps)
            #print(promising2(W,i[0],vcolour))
            #print(i[0])
            if promising2(W,i[0],vcolour):
                colours = colours[1:]
                new_comps.remove(i)
            else:
                vcolour[i[0]] = 0
        if isGoal(vcolour):
            return(vcolour)
        comps = new_comps




    
                



W = [
    [0,1,0,0,0],
    [1,0,1,1,0],
    [0,1,0,1,0],
    [0,1,1,0,1],
    [0,0,0,1,0]
]

W = [
    [0,1,0,1,0,0],
    [1,0,1,0,1,0],
    [0,1,0,0,0,1],
    [1,0,0,0,1,0],
    [0,1,0,1,0,1],
    [0,0,1,0,1,0]]


W = [
    [0,1,0,0,1,1,1,0],
    [1,0,1,0,0,1,0,0],
    [0,1,0,1,0,0,1,0],
    [0,0,1,0,0,1,1,1],
    [1,0,0,0,0,1,0,0],
    [1,1,0,1,1,0,0,0],
    [1,0,1,1,0,0,0,1],
    [0,0,0,1,0,0,1,0]
]

n = len(W)
vcolour = [0]*n


#==================Choose colour outputs==================
#colours = ["r","g","b","y"][:3]
#colours = [1,2,3,4][:3]
colours = ["red","blue","green","y"][:3]




#================Choose which program to run=====================
m_colouring(W,-1,vcolour,n,colours)
#print(m_colouring_heuristic(W,colours)) # something I was looking at, but it is not optimal
