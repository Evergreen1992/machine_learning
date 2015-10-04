#encoding:utf-8
#KNN算法例子 -- 手写数字识别
from numpy  import *
from posix import listdir
from KNN import classify0

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
    trainingFileList = listdir('trainingDigits')
    m = len(trainingFileList)
    trainingMat = zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('trainingDigits/%s'%fileNameStr)
    testFileList = listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnserTest = img2vector('testDigits/%s'%fileNameStr)
        classifierResult = classify0(vectorUnserTest,trainingMat, hwLabels, 3)
        print "the classifier came back with : %d, the real answer is : %d"%(classifierResult, classNumStr)
        if( classifierResult != classNumStr): 
            errorCount += 1.0
    print "\n the total number of errors is : %d "%errorCount
    print "\n the total error rate is : %f "%(errorCount/float(mTest))
            
handwritingClassTest()