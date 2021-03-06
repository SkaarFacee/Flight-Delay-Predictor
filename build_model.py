# -*- coding: utf-8 -*-
"""build_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lf08W2UcNtM8t2Dp39n3ufwML7r0Nirs
"""

import numpy as np
import pandas as pd
import joblib

item = pd.read_csv("data.csv")

item.drop("Unnamed: 0",axis=1,inplace=True)

X=item.drop(["bin"],axis=1)
y=item.loc[:,'bin'].values
from sklearn.model_selection import train_test_split
X_train,X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,stratify=y)

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())])
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value=42)),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))])

temp=item.drop(['bin'], axis=1)
numeric_features = list(temp.columns[(temp.dtypes == 'int64') | (temp.dtypes == 'float64')])
categorical_features = list(temp.columns[temp.dtypes == 'object'])

from sklearn.compose import ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
                  ('num', numeric_transformer, numeric_features),
                  ('cat', categorical_transformer, categorical_features)])

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
rf = Pipeline(steps=[('preprocessor', preprocessor),
                      ('forest', RandomForestClassifier())])
rf.fit(X_train,y_train)

# Saving model 
joblib.dump(rf,'model')

