


from multiprocessing.dummy import JoinableQueue


def lst_to_dic(W):
    ks = ["Job","Deadline", "Profit"]
    oupt = []
    for i in W:
        dic = {}
        for j in range(3):
            dic[ks[j]] = i[j]
        oupt.append(dic)
    return(oupt)
        




def Check_if_possible_schedual(joblst):
    joblst.sort(key=lambda x: x["Deadline"])
    for i in range(len(joblst)):
        if i+1 > joblst[i]["Deadline"]:
            return False

    return True

def Deadline_Schedual(joblst):
    joblst.sort(reverse = True, key=lambda x: x["Profit"])
    current_Schedual = []
    i = 0
    while i < len(joblst):
        #print(current_Schedual)
        current_Schedual.append(joblst[i])
        if not Check_if_possible_schedual(current_Schedual):
            current_Schedual.remove(joblst[i])
        pnt = []
        for j in current_Schedual:
            pnt.append(j["Job"])
        print(pnt)
        i += 1
    
    profit = 0
    schedual = []
    for i in current_Schedual:
        schedual.append(i["Job"])
        profit += i["Profit"]

    print("Schedual: " +str(schedual) )
    print("Profit: " +str(profit) )






W = [
    [1,3,40],
    [2,4,20],
    [3,3,60],
    [4,2,25],
    [5,1,15],
    [6,1,40],
    [7,2,50]
    ]


W1 = [
    [1,3,7],
    [2,2,2],
    [3,3,9],
    [4,1,8]
    ]

W2 = [
    [1,2,40],
    [2,4,15],
    [3,3,60],
    [4,2,20],
    [5,3,10],
    [6,1,45],
    [7,1,55]
    ]

def print2DArrayOverleaf(W):
    print("\\begin{table}[h] \n \\centering")
    cs= "c|" * len(W[0])
    print("\\begin{tabular}{|" + cs + "}")
    print("\\hline")
    for i in W:
        k = []
        for j in i:
            k.append(str(j))
        print("&".join(k) + "\\\\")
        print("\\hline")
    print("\\end{tabular}")
    print("\\end{table}")

 #
W3 = [
['a', 27],
['e', 22],
['h', 33],
['j', 25],
['o', 24],
['r', 20],
['u', 17]
]
#joblst = lst_to_dic(W2)
#print2DArrayOverleaf(W3)
#Deadline_Schedual(joblst)

s = [8, 16, 38, 113, 15, 30, 49, 14, 20]
W3.sort(key = lambda x: x[1])
print(W3)