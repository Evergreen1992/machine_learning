#encoding=utf-8
#使用apriori进行关联分析
print "----------------Apriori关联分析----------------"

def loadDataSet():
    return [[1,3,4],
            [2,3,5],
            [1,2,3,5],
            [2,5]]

def createC1(dataSet):
    c1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in c1:
                c1.append([item])
    c1.sort()
    return map(frozenset, c1)

def scanD(D, Ck, minSupport):
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if tid.issubset(can):
                if not ssCnt.has_key(tid):
                    ssCnt[tid] = 1
                else:
                    ssCnt[tid] += 1
    numItems = float(len(Ck))
    retList = []
    supportData = {}
    for key in ssCnt :
        support = ssCnt[key] / numItems
        if support >= minSupport:
            retList.insert(0, key)
        supportData[key] = support
    return retList, supportData

def aprioriGen(LK, k):
    retList = []
    lenLk = len(LK)
    for i in range(lenLk):
        for j in range(i + 1, lenLk):
            L1 = list(LK[i])[:k - 2]
            L2 = list(LK[j])[:k - 2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append(LK[i] | LK[j])
    return retList

def apriori(dataSet, minSupport = 0.5):
    C1 = createC1(dataSet)
    D = map(set, dataSet)
    L1 , supportData = scanD(C1, D, minSupport)
    L = [L1]
    k = 2
    while( len(L[k - 2]) > 0):
        Ck = aprioriGen(L[k - 2], k)
        Lk , supK = scanD(Ck, D, minSupport)
        supportData.update(supK)
        L.append(Lk)
        k += 1
    return L, supportData
###########################################################################################
dataSet = loadDataSet()
c = createC1(dataSet)
ck = map(set, dataSet)
retList, supportData = scanD(c, ck, 0.5)

for item in retList:
    print item , supportData[item]