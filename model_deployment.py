import pandas as pd
from matplotlib import pyplot
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error
from math import sqrt

def predict():
  data = pd.read_csv('items.csv')
  dataT = data.T
  item1 = dataT.iloc[1:,1]
  # split dataset
  X = item1.values
  train, test = X[1:len(X)-7], X[len(X)-7:]
  # train autoregression
  model = AutoReg(train, lags=14)
  model_fit = model.fit()
  # make predictions
  predictions = model_fit.predict(start=len(train), end=len(train)+len(test)-1, dynamic=False)
  print(predictions)
  rmse = sqrt(mean_squared_error(test, predictions))
  print('Test RMSE: %.3f' % rmse)

predict()
