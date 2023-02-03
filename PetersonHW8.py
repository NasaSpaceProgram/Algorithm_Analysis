from math import inf

    
def dijkstra(W):
    n = len(W)
    F = []
    touch  = [0]
    length = [0]
    for i in range(1,n): # initialize our lists to the inital values 
        touch.append(0)
        length.append(W[0][i])

    for v in range(n-1):
        #print(touch)
        #print(length)
        min = inf
        for i in range(1,n): # look for the nearest node to add to the blob
            if 0 <= length[i] and length[i] <= min: 
                min = length[i]
                vnear = i
        e = (touch[vnear],vnear) # add the edge from touch[vnear] to vnear to our list F 
        F.append(e)
        for i in range(1,n): # look for shorter paths now possible with the new node in the "blob"
            if length[vnear] + W[vnear][i]< length[i]: 
                length[i] = length[vnear] + W[vnear][i] 
                touch[i] = vnear
        length[vnear] = -1 # this node is no longer considered for V near 

    return(F)



W2 = [[0,5,2,inf,inf,inf,inf,inf,inf],
     [inf,0,inf,3,7,inf,inf,inf,inf],
     [inf,2,0,inf,inf,inf,9,inf,inf],
     [inf,inf,3,0,2,inf,6,inf,inf],
     [inf,inf,inf,inf,0,8,5,7,inf],
     [inf,inf,inf,inf,inf,0,inf,inf,4],
     [inf,inf,inf,inf,inf,inf,0,2,inf],
     [inf,inf,inf,inf,inf,3,inf,0,inf],
     [inf,inf,inf,inf,inf,inf,inf,inf,0]
    ]
W = [[0,   7,   4,   6,   1],
     [inf, 0,   inf, inf, inf],
     [inf, 2,   0,   5,   inf],
     [inf, 3,   inf, 0,   inf],
     [inf, inf, inf, 1,   0]
    ]



print("output of Dijkstra indexing at 0")
print(dijkstra(W2))
