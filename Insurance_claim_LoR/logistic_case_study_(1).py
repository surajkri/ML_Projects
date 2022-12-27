# -*- coding: utf-8 -*-
"""logistic_case_study (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1idF69kKJLAPeukG8hfvY4qxAOnBKXJAY
"""

import numpy as np
import pandas as pd

data=pd.read_csv("/content/insurance2.csv")

data.head()

x=data.drop(['insuranceclaim'],axis=1)
y=data['insuranceclaim']

x.head()

x.describe()

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)

from sklearn.linear_model import LogisticRegression
logmodel=LogisticRegression()

logmodel.fit(x_train,y_train)

predictions=logmodel.predict(x_test)

print(predictions)

from sklearn.metrics import confusion_matrix,accuracy_score
cm=confusion_matrix(y_test,predictions)
ac=accuracy_score(y_test,predictions)

print(cm)

print(ac)

