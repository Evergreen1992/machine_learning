import matplotlib.pyplot as plt
from numpy  import *
import operator

def displayImg(a, b):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(a[1], b[1])
    plt.show()
    
a=[[1,2,3],[4,5,6],[7,8,9]]
displayImg(a, a)