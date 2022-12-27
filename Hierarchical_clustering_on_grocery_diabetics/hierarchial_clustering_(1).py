# -*- coding: utf-8 -*-
"""hierarchial_clustering (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18I-S1uVA7zyznYBbrNR5nW912tG89NsL
"""

import numpy as np
import pandas as pd

data=pd.read_csv("/content/Wholesale customers data.csv")

data.head()

import matplotlib.pyplot as plt

#creating dendrogram
import scipy.cluster.hierarchy as sch 
plt.title('Wholesale Dendrogram')
dendrogram=sch.dendrogram(sch.linkage(data,method='ward'))

from sklearn.cluster import AgglomerativeClustering
cluster=AgglomerativeClustering(n_clusters=3,affinity='euclidean',linkage='ward')
cluster.fit_predict(data)

new_data=pd.read_csv("/content/diabetes.csv")

new_data.head()

import scipy.cluster.hierarchy as sch 
plt.title('Diabetes Dendrogram')
dendrogram=sch.dendrogram(sch.linkage(new_data,method='ward'))

