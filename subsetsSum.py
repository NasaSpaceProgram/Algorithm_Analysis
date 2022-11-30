from copy import deepcopy
def subSum(W, w, notincludedNum, included= [] , incN = 0, i = -1):
    nincN = notincludedNum 
    if promising(W,w, incN, nincN, i):
        if incN == W:
            print(included)
        else:
            i+=1
            subSum(W, w, nincN - w[i], included= deepcopy(included) + [w[i]] , incN = incN + w[i], i = i)
            subSum(W, w, nincN - w[i], included= deepcopy(included) , incN = incN, i = i)

def promising(W,w, incN, nincN, i):
    return((incN + nincN >= W ) and (incN == W or incN + w[i + 1] <= W ))

def subSumInt(W,w, inc = []):
    n = sum(inc)
    if n <= W:
        if n == W:
            print(inc)
        else:
            if len(w) >= 1:
                subSumInt(W,w[1:], inc = deepcopy(inc) + [w[0]])
                subSumInt(W,w[1:], inc = deepcopy(inc))
W = 17
w = [4,6,7,11]
W = 13
w = [3,4,5,6]

W = 52
w = [2,10,13,17,22,42]


subSum(W, w, sum(w))
#subSumInt(W,w)