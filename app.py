from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route("/")
def hello():
    print("initial HTML call to render index html") 
    return render_template('index.html')

@app.route('/predict', methods = ['GET','POST'])
def result():
    if request.method == 'GET':
         print('GET') 
    if request.method == 'POST':
        print('POST')
        height  = request.form["height"]
        height = int(height)
        print(height)
        weight = model.predict([[height]])

    return render_template('index.html', prediction_text="Weight = {}".format(weight))
    
if __name__ == "__main__":
    app.run(debug=True)