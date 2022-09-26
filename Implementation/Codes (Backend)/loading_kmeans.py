# -*- coding: utf-8 -*-
"""Loading_Kmeans.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_CxbfTciIZURaSbg8jiibVr1RA4WybW1
"""

import pickle
from sklearn.cluster import KMeans
import pandas as pd

loaded_model = pickle.load(open('kmeans_knowledge_cluster.sav', 'rb'))
testdf=pd.read_csv("KnowledgeCleansed_Clusters.csv")
testdf=testdf.set_index("Class")
skills=pd.read_csv("knowledgecleansed.csv")
skills.head()

target=skills["Title"]
data=skills.drop("Title",axis=1)
feature_name=data.columns
test=data[:1]
test

result = loaded_model.predict(test)
print("The test data belongs to Class: ", result[0])
df=testdf.loc[testdf.index==result[0]]
print("The jobs are:",df.values)

df