#coding=utf-8
import pandas as pd
import numpy as np

#创建序列
s=pd.Series([1,3,5,6,8, np.nan])

#创建dataframe数据结构
dates=pd.date_range("20160116",periods=10)
df=pd.DataFrame(np.random.randn(10,4),index=dates,columns=list('ABCD'))

df2=pd.DataFrame({'A':[1,2,4,3],
                  'B':pd.Timestamp("20160116"),
                  'C':np.array([3]*4, dtype='int32'),
                  'D':pd.Series(1,index=list(range(4)),dtype='float32'),
                  'E':pd.Categorical(['星期一',"星期二","星期三","星期四"]),
                  'F':'其他信息'})
df3=pd.DataFrame({'A':[1,3,4,2],
                  'B':[1,3,4,2],
                  'C':[1,3,4,2],
                  'D':[1,3,4,2]})
#查看数据类型
#print df2.dtypes

#查看frame头部和尾部的行
#print df2.head(1)
#print df2.tail(1)

#显示索引
#print df2.index
#print df2.columns
#print df2.values

#数据快速统计汇总
#print df2.describe()

#数据转置
#print df2.T

#按轴进行排序
#print df3.sort_index(axis=1, ascending=False)

#按内容排序
#print df3.sort(columns='A')

#print df2['C']

#print df3[1:4]

#获取特定的值
#print df3.iloc[0,0]

#布尔索引
#通过一个单独列的值来选择数据
#print df3[df3.A > 2]
#print df3[df3 > 3]


#设置新的列
s1=pd.Series([88,99,11,22])
df3['H']=s1

print df3
print "---------------------------------------------------"

df3.at[0,'H']=10086

df3.loc[:,'D']=np.array([9] * 4)

#去掉缺失值
df3.dropna(how='any')
#补充缺失值
df3.fillna(value=5)
#对布尔数据进行填充
#df3.isnull(df3)


#写入csv文件
df3.to_csv('test.cvs')


#print pd.read_csv('test.cvs')






