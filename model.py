# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 17:08:28 2022

@author: harsh
"""

import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# reading the data.
df = pd.read_csv('cars24-price.csv')

X = df.drop('selling_price', axis=1)
Y = df['selling_price']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

# Import the Algorithm 

#from sklearn.tree import DecisionTreeRegressor

# created the model
model = LinearRegression()
#dtr = DecisionTreeRegressor()

# training of the model
model.fit(X_train, y_train)
#dtr.fit(X_train, y_train)
filename="model.pkl"
pickle_out = open(filename, "wb")
pickle.dump(model, pickle_out)
pickle_out.close()