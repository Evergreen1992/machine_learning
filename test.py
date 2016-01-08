from numpy import *
from numpy import linalg as la

'''
a=[0,0]
b=[3,4]
 
print la.norm(array(a) - array(b))

mm = array([[1,2,3],[4,5,6]])
nn = array([[1,2,3],[4,5,6]])

print mm * nn
'''
ma = mat([1,2,3])
mn = mat([1,2,3])
c = mat([[1,2,3],
         [4,5,6]])
print nonzero(c[1,:].A == 5)

print nonzero(logical_and(c[:,0] > 0 , c[:,1] > 0))[1]