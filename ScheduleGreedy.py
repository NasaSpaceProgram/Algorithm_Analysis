from copy import deepcopy
def ListtoTable(lst):
    oupt = []
    for row in lst:
        r = {"Job":row[0],"Deadline":row[1],"Profit":row[2] }
        oupt.append(r)
    return(oupt)

def isFeasableSchedual(deadlines):
    deadlines.sort()
    t = 1
    for d in deadlines:
        if d < t:
            return(False)
        t +=1
    return(True)

def schedule(W):
    W.sort(reverse = True, key = lambda x: x["Profit"])
    K = [] # list of deadlines
    J = [] # list of jobs
    for j in W:
        oldK = deepcopy(K)
        K.append(j["Deadline"])
        if isFeasableSchedual(K):
            J.append(j)
            J.sort(key = lambda x: x["Deadline"])
        else:
            K = oldK
    return(J)

def main(W):
    Jobs = schedule(W)
    profit = 0
    print()
    print("===Jobs===")
    for j in Jobs:
        print(j)
        profit += j["Profit"]
    print("==========")
    print("==Profit==")
    print(profit)
    print()

        


W1 = [
    [1,2,30],
    [2,1,35],
    [3,2,25],
    [4,1,40]
]

W2 = [
    [1,3,40],
    [2,4,20],
    [3,3,60],
    [4,2,25],
    [5,1,15],
    [6,1,40],
    [7,2,50]
]

W3 = [
    [1,5,25],
    [2,3,70],
    [3,1,75],
    [4,2,35],
    [5,2,55],
    [6,2,60],
    [7,4,30],
    [8,3,40]
]


W = ListtoTable(W3)

main(W)