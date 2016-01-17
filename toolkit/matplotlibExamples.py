#coding=utf-8

####################
#   matplotlib例子      #
####################

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
"""
#绘制sinx 
#0到10之间产生1000个数
x=np.linspace(0,10,1000)
y=np.sin(x)
z=np.cos(x)
#图像大小
plt.figure(figsize=(8,4))
#绘制sin(x)
plt.plot(x,y,label="sin(x)",color="red",linewidth=2)
plt.plot(x,z,"b--",label="cos(x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin(x) example")
#y轴的范围
plt.ylim(-3, 3)
#显示图示
plt.legend()
plt.show()
"""
#####################################################
"""
x=np.arange(0,5,0.1)
y=np.linspace(0, 10, 1000)
df=pd.DataFrame([0,1,2,3,4,5,6,7,8,9])
line=plt.plot(x,x)
lines=plt.plot(y,np.log10(y),y,np.cos(y))
#调用setp设置多个line2d对象的多个属性值
plt.setp(lines,color="red",linewidth=2)
plt.show()
"""

####################################################
"""
plt.figure(1)
plt.figure(2)
ax1=plt.subplot(211)
ax2=plt.subplot(212)
x=np.linspace(0,3,100)
for i in range(5):
    plt.figure(1)#选择图表
    plt.plot(x,np.exp(i*x/3))
    plt.sca(ax1)#选择子图
    plt.plot(x,np.sin(i*x))
    plt.sca(ax2)#选择子图
    plt.plot(x,np.cos(i*x))
plt.show()
"""

########################################
"""
dfx=pd.DataFrame([1,3,2,5,6,2])
dfy=pd.DataFrame([2,3,4,1,2,-1])
x=np.linspace(0,10,100)
y=np.linspace(1,5,100)
#o表示散点图
plt.plot(dfx,dfy,'o')
plt.xlim(-5,10)
plt.ylim(-5,10)
plt.show()
"""
#################################################













