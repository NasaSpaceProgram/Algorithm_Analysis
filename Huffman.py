
# {"f": None, "Prefix": "", "C1":None, "C2":None}
def MakeTable(lst):
    oupt = []
    for row in lst:
        oupt.append({"Char":row[0],"f":row[1], "Prefix": ""})
    return(oupt)

def MakeTree(T):
    while len(T) > 1:
        T.sort(key = lambda x: x["f"])
        T = T[2:] + [{"f": T[0]["f"]+T[1]["f"], "Prefix": "", "C1":T[0], "C2":T[1]}]
    return(T[0])

def EncodeNode(T,lst):
    if "C1" not in T["C1"].keys():
        T["C1"]["Prefix"] = T["Prefix"] + "0"
        lst.append(T["C1"])
    else:
        if T["C1"]:
            T["C1"]["Prefix"] = T["Prefix"] + "0"
            EncodeNode(T["C1"],lst)

    if "C1" not in T["C2"].keys():
        T["C2"]["Prefix"] = T["Prefix"] + "1"
        lst.append(T["C2"])
    else:
        if T["C2"]:
            T["C2"]["Prefix"] = T["Prefix"] + "1"
            EncodeNode(T["C2"],lst)

def MakeEncoding(T):
    lst = []
    R = MakeTree(T)
    EncodeNode(R,lst)
    return(lst)

def main(T):
    enc = MakeEncoding(T)
    totalbits = 0
    print("===Encodings===")
    for c in enc:
        print(c)
        totalbits += c["f"]*len(c["Prefix"])
    print("===============")
    print("===BitsLength===")
    print(totalbits)



lst = [
    ["a",5],
    ["b",9],
    ["c",12],
    ["d",13],
    ["e",16],
    ["f",45],
    ["g",21]
]

T = MakeTable(lst)
main(T)