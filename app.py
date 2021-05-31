from flask_restful import reqparse
from flask import Flask, jsonify, request
import pandas as pd
from statsmodels.tsa.ar_model import AutoReg

app = Flask(__name__)

@app.route('/')
def home():
    print("this is amazing")
    return 'hello'

@app.route('/prediction', methods=['POST'])
def prediction():
  json = request.get_json()
  name = list(json[0].values())
  print(name)
  data = pd.read_csv('items.csv')
  dataT = data.T
  itemnames = dataT.iloc[0,0:]
  var = name[0]
  print(var)
  found = 0
  for i in range(len(itemnames)):
    itemnames[i] = itemnames[i].replace("  ", " ")
    itemnames[i] = itemnames[i].replace("mm ", "mm")
    itemnames[i] = itemnames[i].replace("Inch ", "Inch")
    if itemnames[i] == var:
        found = i
  item1 = dataT.iloc[1:,i]
  # split dataset
  X = item1.values
  train, test = X[1:len(X)-7], X[len(X)-7:]
  # train autoregression
  model = AutoReg(train, lags=14)
  model_fit = model.fit()
  # make predictions
  predictions = model_fit.predict(start=len(train), end=len(train)+len(test)-1, dynamic=False)
  print(predictions)
  weekly = predictions.sum()//1
  print(weekly)
  return jsonify({'prediction': str(weekly)})

if __name__ == '__main__':
    app.run(debug=True)
