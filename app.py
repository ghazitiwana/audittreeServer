from flask_restful import reqparse
from flask import Flask, jsonify, request
import pandas as pd
from statsmodels.tsa.ar_model import AutoReg

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello'

@app.route('/prediction', methods=['POST'])
def prediction():
  data = pd.read_csv('items.csv')
  dataT = data.T
  item1 = dataT.iloc[1:,1]
  # split dataset
  #X = item1.values
  #train, test = X[1:len(X)-7], X[len(X)-7:]
  # train autoregression
  #model = AutoReg(train, lags=14)
  #model_fit = model.fit()
  # make predictions
  #predictions = model_fit.predict(start=len(train), end=len(train)+len(test)-1, dynamic=False)
  #print(predictions)
  return "woohoo"

if __name__ == '__main__':
    app.run(debug=True)
