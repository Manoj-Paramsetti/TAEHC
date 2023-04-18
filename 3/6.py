# Splitting the dataset into the Training set and Test sete
import numpy as np
import pandas as pd

Dataset = pd.read_csv("datasets/Heart.csv")

x = Dataset.iloc[:, :-1].values 
print(x)

Dataset.info()

print(Dataset.describe())

Data = Dataset.fillna(0)
x = Data.iloc[:, :-1].values 
print(x)
Data.info()

Datamean = Dataset.fillna(Dataset.mean())
x = Datamean.iloc[:, :-1].values 
print(x)
Datamean.info()

cols = ['Oldpeak']
Datamean = Datamean.drop(cols, axis=1)
x = Datamean.iloc[:, :-1].values 
print(x)
Datamean.info()

X = Datamean.values
y = Datamean['AHD'].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
print("Training Samples\n",X_train)
print("Testing Samples\n",X_test)