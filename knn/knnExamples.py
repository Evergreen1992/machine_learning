#encoding:utf-8
#KNN算法例子 -- 手写数字识别
from numpy  import *
import os, sys
import operator


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


#图像文件(32x32)转化成一维数组
def  img2vector(filename):
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32 * i + j] = int(lineStr[j])
    return returnVect

#手写数字识别系统的测试例子
def handwritingClassTest():
    hwLabels = []
    trainingFileList = os.listdir('trainingDigits')
    m = len(trainingFileList)
    trainingMat = zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('trainingDigits/%s'%fileNameStr)
    testFileList = os.listdir('test')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        #classNumStr = int(fileStr.split('_')[0])
        vectorUnserTest = img2vector('testDigits/%s'%fileNameStr)
        classifierResult = classify0(vectorUnserTest,trainingMat, hwLabels, 3)
        print classifierResult
        if( classifierResult != classNumStr): 
            errorCount += 1.0
    #print "\n the total number of errors is : %d "%errorCount
    #print "\n the total error rate is : %f "%(errorCount/float(mTest))
            
handwritingClassTest()