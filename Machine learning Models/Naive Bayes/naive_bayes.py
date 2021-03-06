# -*- coding: utf-8 -*-
"""Naive Bayes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18U2qOilhtVa-O7Uj35AeWgL8I9e43Z4C
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

df=pd.read_csv('/content/drive/My Drive/train.csv')
df.isnull().sum()

dfdrop=df.drop(['PassengerId','Name','SibSp','Parch','Ticket','Cabin','Embarked'],axis='columns')

dfdrop.head()

Y=dfdrop['Survived']
Y.head()

Da=dfdrop.drop(['Survived'], axis='columns')
Da.head()

dummies=pd.get_dummies(Da.Sex)
dummies.head()

new=pd.concat([Da,dummies], axis='columns')
new.head()

new=new.drop(['Sex'], axis='columns')
new.head()

new.isnull().sum()

new.Age.median()

new.Age=new.Age.fillna(new.Age.median())
new.isna().sum()

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(new,Y,test_size=0.2)

from sklearn.naive_bayes import GaussianNB
model=GaussianNB()

model.fit(x_train,y_train)

x_test[:5]

y_test.head(5)

model.predict(x_test[:5])

model.score(x_test,y_test)

model.predict_proba(x_test[:5])