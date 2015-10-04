#encoding:utf-8
#kNN算法
from numpy  import *
import operator

def createDataSet():
    group = array(
                   [
                    [1.0, 1.1],
                   [1.0, 1.0],
                   [0, 0],
                   [0, 0.1]
                   ])
    labels = ['A','A','B','B']
    return group, labels

#计算距离。并选择距离最近的前k个节点。
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0] #返回矩阵行数
    diffMat = tile(inX, (dataSetSize,1))-dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)#计算矩阵每行的和
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()#排序。并返回下标。
    classCount = {}
    for i in range(k):#选择距离最小的前k个。
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1#D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse = True)
    return sortedClassCount[0][0]

#将文本文件数据转换成矩阵
def  file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMax = zeros((numberOfLines,2))
    classLabelVector = []
    index = 0 
    for line in arrayOLines:
        line = line.strip()#去掉回车符号
        listFromLine = line.split('\t')
        returnMax[index, : ] = listFromLine[0:2]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMax, classLabelVector

#main function
#group, labels = createDataSet()
#print classify0([0,0] ,group, labels, 3)
mat, labels = file2matrix("data.txt")#获取学习数据
print "(1: A, 2: B, 3:C)数据类型是:  %d"%classify0([0,0] ,mat, labels, 2) 
