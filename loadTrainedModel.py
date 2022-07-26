import pickle
import numpy as np
from pandas.core.frame import DataFrame
import sklearn
from sklearn import neighbors, metrics
from sklearn.model_selection import train_test_split
import pandas as pd

data = pd.read_csv('TongHopDiemSinhVien_clean1.csv')

X = data.drop('Chuyên ngành', axis=1)
y = data.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(
      X, y, test_size=0.2, random_state=346)

def loadModel():
    global trainedModel
    with open('model_pickle','rb') as f:
        trainedModel = pickle.load(f)

def predict(X):
    feature = data.columns[0:13].tolist()
    X_valid = pd.DataFrame()
    for i in range(13):
        X_valid.loc[0,feature[i]] = X[i]
    y_pred = trainedModel.predict(X_valid)
    return y_pred


