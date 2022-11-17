import pandas as pd
import csv
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori,association_rules

#input datadet is unstructured so hard to read with pandas
#use csv instead
#convert it to list
dataset=[]
with open('Market_Basket_Optimisation.csv') as file:
    reader=csv.reader(file,delimiter=',')
    for row in reader:
      dataset+=[row]
print(dataset[0:10])

#ML model acn not process unstructured data
#convert given dataset to structured data

te=TransactionEncoder()
x=te.fit_transform(dataset)

#convert this structured dataset to a dataframe with rows and columns
df=pd.DataFrame(x,columns=te.columns_)
print(df.head())

#Apriori algorithm
#1.To find frequent itemsets
freq_itemset=apriori(df,min_support=0.05,use_colnames='True')
print(freq_itemset)

#2.To find the rules
rules=association_rules(freq_itemset,metric='lift',min_threshold=1.1)
rules=rules[['antecedents','consequents','support','confidence']]
print(rules)

#recommending for new entry
new=rules[rules['antecedents']=={'eggs'}]
print(new)