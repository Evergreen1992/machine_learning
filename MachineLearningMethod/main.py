import numpy as np

print "...................genarate test dataset...................."
import numpy as np
from sklearn.datasets import make_classification
X,y = make_classification(1000,n_features=20,n_informative=2, n_redundant=2,n_classes=2,random_state=0)

from pandas import DataFrame



df = DataFrame(np.hstack((X,y[:,None])),columns = range(20) + ["class"])
#print df[:10]

import matplotlib.pyplot as plt
import seaborn as sns


_ = sns.pairplot(df[:1000],vars=[8,11,12,14,19],hue="class",size=1.5)
plt.axis([-5,5,-5,5])
plt.show()


import matplotlib.pyplot as plt
plt.figure(figsize=(12,10))
_ = sns.corrplot(df,annot=False)
plt.show()

