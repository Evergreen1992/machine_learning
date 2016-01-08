#encoding=utf-8
from numpy import *
from numpy import linalg as la

print ".......SVD奇异值分解，进行数据降维处理........."

def loadExData():#用户评分数据
    return mat([
            [4,4,0,2,2],
            [4,0,0,3,3],
            [4,0,0,1,1],
            [1,1,1,2,0],
            [2,2,2,0,0],
            [1,1,1,0,0],
            [5,5,5,0,0]
            ])

def eulidSim(inA, inB):#欧氏距离计算
    return 1.0 / (1.0 + la.norm(inA - inB ))

def standEst(dataMat, user, simMeas, item):#计算未评分的item的预计得分
    n = shape(dataMat)[1]
    simTotal = 0.0
    ratSimTotal = 0.0
    for j in range(n):
        userRating = dataMat[user,j]
        if userRating == 0 : continue
        print "--------------------------------------------------------"
        print "j = %d"%j,", item = %d"%item
        print "userRating:%d "%userRating
        overLap = nonzero(logical_and(dataMat[:,item].A > 0 , dataMat[:,j].A > 0))[0]
        if len(overLap) == 0 : 
            similariTy = 0
        else:
            print "相似度计算："
            print dataMat[overLap,item]
            print "....."
            print dataMat[overLap,j]
            similariTy = simMeas(dataMat[overLap,item], dataMat[overLap,j]) 
        print "similarity is : %f"%(similariTy)
        simTotal += similariTy
        ratSimTotal += similariTy * userRating
    if simTotal == 0 :
        return 0
    else:
        return ratSimTotal / simTotal
    
def recomend(dataMat, user, N = 3, simMeas = eulidSim, estMethod = standEst):
    unratedItems = nonzero(dataMat[user,:].A == 0)[1]
    if len(unratedItems) == 0:
        return "you rated everything"
    itemScores = []
    for item in unratedItems:
        #计算未评分的item的预估计得分。
        estimatedScore = estMethod(dataMat, user, simMeas, item)
        itemScores.append((item, estimatedScore))
    return sorted(itemScores, key = lambda jj : jj[1], reverse = True)[:N]

#test cases
dataMat = loadExData()
result = recomend(dataMat, 2)
for item in result:
    print item ,