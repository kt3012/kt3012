import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gre=pd.read_csv("Admission_Predict.csv")

#to convert the continuous values of 'Chance of Admit ' in categorical values i.e. 0 and 1
from sklearn.preprocessing import Binarizer
bi=Binarizer(threshold=0.80)
gre['Chance of Admit ']=bi.fit_transform(gre[['Chance of Admit ']])
print(gre.head())

a=gre.drop("Chance of Admit ", axis = 1)#input variable
b=gre['Chance of Admit ']#output variable
b=b.astype('int')#float to int
sns.countplot(x=b)
plt.show()

from sklearn.model_selection import train_test_split
atr,ate,btr,bte=train_test_split(a,b,test_size=0.2,random_state=1)

from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier(random_state=1)
dt.fit(atr,btr)

bpr=dt.predict(ate)
result=pd.DataFrame({'actual':bte,'predicted':bpr})
print(result)

from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, classification_report
cm=ConfusionMatrixDisplay.from_predictions(bte,bpr)
plt.show()

score=accuracy_score(bte,bpr)
print(score)

cf=classification_report(bte,bpr)
print(cf)

#for new entry
new=[[136,314,109,4,3.5,4.0,8.77,1]] #should be 2D array
p=dt.predict(new)[0]
print(p)

#to plot decision tree
from sklearn.tree import plot_tree
plt.figure(figsize=(12,12))
plot_tree(dt, fontsize=8, filled=True,feature_names=a.columns)
plt.show()
