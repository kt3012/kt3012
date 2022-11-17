import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Mall_Customers.csv")
print(df.head())

x=df.iloc[:,3:] #input variable =index location for all rows ,columns 3 onwards i.e. only 3 and 4 columns

from sklearn.cluster import KMeans, AgglomerativeClustering

#1.Elbow method- distance of each point from centroid of its cluster
sse=[] #within sum of errors or sum of squared errors
for k in range(1,16):
    km=KMeans(n_clusters=k)#for k clusters
    km.fit_predict(x)
    sse.append(km.inertia_)

plt.title("Elbow Method") #plot of SSE vs Inertia to get elbow point
plt.xlabel('Value of K')
plt.ylabel('SSE')
plt.xticks(range(1,16))
plt.plot(range(1,16),sse,marker='.',color='red')
plt.show()
#elbow point=5

#2.Silhoutte method- distance of each point from centroid of its cluster and centroid of nearest cluster
from sklearn.metrics import silhouette_score
silh=[]
for k in range(2,16): #has to be min 2 clusters for there to be a nearest cluster
    km=KMeans(n_clusters=k)#for k clusters
    labels=km.fit_predict(x)
    score=silhouette_score(x,labels)
    silh.append(score)

plt.title("Silhouette Method") #plot of SSE vs Inertia to get elbow point
plt.xlabel('Value of K')
plt.ylabel('Silhouette score')
plt.grid()
plt.xticks(range(2,16))
plt.bar(range(2,16),silh,color='cyan')
plt.show()
#max silhouette score at 5
#therefore optimal value for clusters is n=5

km=KMeans(n_clusters=5,random_state=0)
labels=km.fit_predict(x)
plt.title('Clustered data')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.scatter(x['Annual Income (k$)'],x['Spending Score (1-100)'],c=labels)
plt.show()
