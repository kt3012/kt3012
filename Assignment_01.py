import pandas as pd 
df=pd.read_csv("Heart.csv")
print(df)
df.head(303)
shape=df.shape
print(shape)
print(df.notnull())
result=df.isna().sum()
print(result)
result=df.isna().sum().sum()
print(result)
datatypes=df.dtypes
print(datatypes)
c=(df==0).sum(axis=1)
print(c)
print(df['Age'].mean())
new_df=df.filter(['Age','Sex','ChestPain','RestBP','Chol'])
print(new_df)

