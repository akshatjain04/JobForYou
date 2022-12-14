# -*- coding: utf-8 -*-
"""skills.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O6ZzRDt2_SkEx_ajok3xiHAYsnz7xodn
"""

import pandas as pd
skills=pd.read_csv("Knowledge.csv")
skills.head()

columns=skills["Element Name"].unique().tolist()
columns.append("Title")
columns

row=skills["Title"].unique()

results=[]
for title in row:
   
    new_row=[]
    for sk in columns:
        if sk!="Title":
            try:
                val=skills.loc[(skills["Title"]==title) & (skills["Element Name"]==sk),"Importance"].tolist()
                new_row.append(val[0])
            except:
                new_row.append(0)
    
    new_row.append(title)
    results.append(new_row)

DF=pd.DataFrame(results,columns=columns)
DF.to_csv("ImportanceCleansed.csv",index=False)

DF=pd.read_csv("ImportanceCleansed.csv")
DF.head()

target=DF["Title"]
data=DF.drop("Title",axis=1)
feature_name=data.columns

target.head()

from sklearn.preprocessing import LabelEncoder

# Step 1: Label-encode data set
label_encoder = LabelEncoder()
label_encoder.fit(target)

encoded_y = label_encoder.transform(target)
for label, original_class in zip(encoded_y, target):
   print('Original Class: ' + str(original_class))
   print('Encoded Label: ' + str(label))
   print('-' * 12)
from tensorflow.keras.utils import to_categorical

# Step 2: One-hot encoding
one_hot_y = to_categorical(encoded_y)
one_hot_y

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf= clf.fit(data, target)
clf.score(data,target)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=42)

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=200)
rf = rf.fit(data, target)
feature_names=data.columns
target_names=target
print(X_test)

test=DF[:1]
test_target=test["Title"]
test=test.drop("Title",axis=1)
test["Active Listening"]=0
test["Mathematics"]=0
test["Writing"]=3.25
test["Reading Comprehension"]=3.62
test["Critical Thinking"]=0
test["Science"]=0
rf.predict(test)