#encoding=UTF-8
from numpy import *
print "k均值算法"
#加载数据
def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split("\t")
        fltLine = map(float, curLine)
        dataMat.append(fltLine)
    return dataMat
#距离计算
def distEclud(vecA, vecB):
    return sqrt(sum(pow(vecA - vecB, 2)))
def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros())#质心
    for j in range(n):
        minJ = min(dataSet[:,j])
        rangeJ = float(max(dataSet[:,j]) - minJ)
        centroids[:,j] = minJ + rangeJ * random.rand(k, 1)
    return centroids
#开始执行
mat = loadDataSet("data/testSet.txt")
for data in mat:
    print data[0],data[1],
    print ""