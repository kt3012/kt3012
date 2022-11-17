import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

temp=pd.read_csv('temperatures.csv')
print(temp)
head=temp.head()
print(head)
datatype=temp.dtypes
print(datatype)
columns=temp.columns
print(columns)
describe=temp.describe()
print(describe)
null=temp.isnull().sum()
print(null)

a=temp['YEAR']
b=temp['ANNUAL']

a=a.values
a=a.reshape(117,1)

from sklearn import linear_model,metrics
from sklearn.model_selection import train_test_split
atr,ate,btr,bte=train_test_split(a,b,test_size=.20,random_state=1)

from sklearn.linear_model import LinearRegression
lr=linear_model.LinearRegression()
model=lr.fit(atr,btr)

#intercept=model.intercept_
#print("intercept=",intercept)
#coef=model.coef_
#print("coef=",coef)

bpr=model.predict(ate)
print("Predicted value=",bpr)

from sklearn.metrics import mean_absolute_error
mae=mean_absolute_error(bte,bpr)
print("mae=",mae)

from sklearn.metrics import mean_squared_error
mse=mean_squared_error(bte,bpr)
print("mse=",mse)

from sklearn.metrics import r2_score
r2_sq=r2_score(bte,bpr)
print("r2_sq=",r2_sq)
r_sq=lr.score(ate,bte)
print("r_sq=",r_sq)

plt.scatter(atr,btr,color='yellow')
plt.plot(atr,lr.predict(atr),color='red',linewidth=1)
plt.title("Temp vs Year (Training)")
plt.xlabel("Year")
plt.ylabel("Temperature")
plt.show()
plt.scatter(ate,bte,color='cyan')
plt.plot(ate,lr.predict(ate),color='black',linewidth=1)
plt.title("Temp vs Year (Testing)")
plt.xlabel("Year")
plt.ylabel("Temperature")
plt.show()

