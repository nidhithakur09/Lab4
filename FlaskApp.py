import numpy as np
import pickle
import pandas as pd
from flask import Flask, request, render_template, jsonify

app=Flask(__name__)
pickle_in = open("classifier_fish.pkl","rb")
classifier=pickle.load(pickle_in)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = classifier.predict(final_features)
    if (prediction == 0):
        prediction = 'Bream'
    if (prediction == 4):
         prediction = 'Roach'
    if (prediction == 6):
         prediction = 'Whitefish'
    if (prediction == 1):
         prediction = 'Parkki'
    if (prediction == 2):
         prediction = 'Perch'
    if (prediction == 3):
         prediction = 'Pike'
    if (prediction == 5):
         prediction = 'Smelt'
   
   
        
    
    return render_template('index.html', prediction_text='The Name of the fish is {}'.format(prediction))


if __name__=='__main__':
    app.run()