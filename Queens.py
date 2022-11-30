
import copy
def printBoard(col):
    print()
    for i in col:
        row = ["X"] * len(col)
        row[i] = "O"
        print("|".join(row))
    print()

def promising(i,col):
    k = 0
    switch = True
    while k<i and switch:
        if (col[i] == col[k]) or (abs(col[i]-col[k]) == i-k):
            switch  = False
        k += 1
    return(switch)


def queens(i,col,oupt):
    n = len(col)
    j = 0
    if promising(i,col):
        if i == n-1:
            printBoard(col)
            oupt.append(copy.deepcopy(col))
        else:
            for j in range(n):
                col[i+1] = j
                queens(i+1,col,oupt)
    return(oupt)


def findQueens(n):
    col = []
    for j in range(n):
        col.append(0)
    i = -1
    oupt = []
    oupt1 = queens(i,col,oupt)
    print(oupt1)
    print(len(oupt1))

findQueens(7)