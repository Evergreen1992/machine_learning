#encoding:utf-8

from numpy import *

"""使用朴素贝叶斯进行文本分类"""

def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]#1代表侮辱性文字  0代表正常言论
    return postingList, classVec

def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)#集合并集
    return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet):
    returnVect=[0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVect[vocabList.index(word) ] = 1
        else:
            print "the word %s is not in the list"%word
    return returnVect

def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    p0Num = zeros(numWords)
    p1Num = zeros(numWords)
    p0Denom = 0.0; p1Denom = 0.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
        p1Vect = p1Num / p1Denom
        p0Vect = p0Num / p0Denom
    return p0Vect, p1Vect, pAbusive
    

"""

"""
listOPosts, listClasses = loadDataSet()
myVocabList = createVocabList(listOPosts)
trainMat=[]
for postinDoc in listOPosts:
    trainMat.append(setOfWords2Vec(myVocabList, postinDoc))

p0v, p1v , pAb = trainNB0(trainMat, listClasses)

print pAb
print p0v
print p1v
