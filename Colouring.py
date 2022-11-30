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
n = len(W)
vcolour = [0]*n
#colours = ["r","g","b","y"][:3]
colours = [1,2,3,4][:3]
colours = ["red","blue","green","y"][:3]
m_colouring(W,-1,vcolour,n,colours)