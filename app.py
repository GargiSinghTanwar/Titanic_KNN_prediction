import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('/content/drive/My Drive/titanic.pkl','rb')) 

@app.route('/')
def home():
  
    return render_template("index.html")
  
@app.route('/predict',methods=['GET'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    age = int(request.args.get('age'))
    Pclass = int(request.args.get('Pclass'))
    Sex = int(request.args.get('Sex'))
    SibSp = int(request.args.get('SibSp'))
    Parch = int(request.args.get('Parch'))
    fare = int(request.args.get('fare'))
    prediction = classifier.predict([[age,Pclass,Sex,SibSp,Parch,fare]])
    
    print("Survival prediction",prediction)
    if prediction==[1]:
      prediction="You are a survival"
    else:
      prediction="You are not a survival"
        
    return render_template('index.html', prediction_text='survival prediction : {}'.format(prediction))

if __name__ == "__main__":
    app.run(debug=True)