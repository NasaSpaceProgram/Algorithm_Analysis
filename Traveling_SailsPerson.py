from math import inf
def travil(n, W):
    D = {}
    for i in range(1,n+1):
        D[str(i)] = {}
    for i in range(1,n+1):
        D[str(i)]['e'] = W[i-1][0]
    for A in powerset(range(2,n+1))[1:]:
        print(str(tuple(A))+"\\\\")
        for i in range(1,n+1):
            if (i == 1 and A != powerset(range(2,n+1))[-1])or (i in A):
                D[str(i)][str(A)] = "X"
            else:
                posibilities = []
                possibilities2 = []
                for j in A:
                    if len(A) > 1:
                        addon = D[str(j)][str([x for x in A if x != j])]
                    else:
                        #print(D[j])
                        addon = D[str(j)]['e']

                    if addon == "X":
                        addon = 0
                    posibilities.append(W[i-1][j-1]+addon)
                    possibilities2.append(str(W[i-1][j-1]) + "+" + str(addon))
                sufix = "[(" + "), (".join(possibilities2) + ")]"
                prefix = "\,\, D[V"+str(i) +"]" +"["+str(tuple(A))+"] = min" 
                print(prefix + sufix + "\\\\")
                print(prefix + str(posibilities) +  "\\\\")
                #print(posibilities)
                D[str(i)][str(A)] = min(posibilities)
    D[str(1)]['e'] = "X"
    return(D)




from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    sets = list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    oupt = []
    for set in sets:
        oupt.append(list(set))
    return oupt


def powerset_strings(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    sets = list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    oupt = []
    for set in sets:
        app = "$\{"
        for i in set:
            app += "V_" + str(i) + ": "
        app += "\}$"
        oupt.append(app)
    return oupt






W = [
    [0,8,13,18,20],
    [3,0,7,8,10],
    [4,11,0,10,7],
    [6,6,7,0,11],
    [10,6,2,1,0]
    ]
n = 5

W = [
    [0,2,9,inf],
    [1,0,6,4],
    [inf,7,0,8],
    [6,3,inf,0]
    ]



n = 4



D = travil(n, W)

f = open("TS_oupt.csv","w")
#header 
header = ["D, $\{\}$"] + powerset_strings(range(2,n+1))[1:]
f.write(",".join(header))
f.write("\n")
j = 1
for key1 in D.keys():
    row = D[key1]
    f.write("$V_" + str(j)+"$")
    for i in row.keys():
        f.write(",")
        f.write(str(row[i]))
    f.write("\n")
    j += 1



f.close()
