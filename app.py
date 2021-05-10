from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import pandas as pd
import sklearn
import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = joblib.load('filename.pkl')  
  
# Use the loaded model to make predictions 

@ app.route('/', methods = ['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()


@ app.route("/predict", methods = ['POST'])
def predict():
    if request.method == 'POST':
        battery_power = int(request.form['battery_power'])
        clock_speed = float(request.form['clock_speed'])
        blue = request.form['blue']
        if blue == 'Yes':
            blue = 1
        else :
            blue = 0
        dual_sim = request.form['dual_sim']
        if dual_sim == 'Yes':
            dual_sim = 1
        else :
            dual_sim = 0
        four_g = request.form['four_g']
        if (four_g == 'Yes'):
            four_g = 1
        else :
            four_g = 0
        fc = int(request.form['fc'])
        int_memory=int(request.form['int_memory'])
        m_dep = float(request.form['m_dep'])
        mobile_wt = int(request.form['mobile_wt'])
        n_cores = int(request.form['n_cores'])
        pc = int(request.form['pc'])
        px_height = int(request.form['px_height'])
        px_width = int(request.form['px_width'])
        ram = int(request.form['ram'])
        sc_h = int(request.form['sc_h'])
        sc_w = int(request.form['sc_w'])
        talk_time = int(request.form['talk_time'])
        three_g = request.form['three_g']
        if (three_g == 'Yes'):
            three_g = 1
        else :
            three_g = 0
        touch_screen = request.form['touch_screen']
        if (touch_screen == 'Yes'):
            touch_screen = 1
        else :
            touch_screen = 0
        wifi = request.form['wifi']
        if (wifi == 'Yes'):
            wifi = 1
        else :
            wifi = 0
        
        price = model.predict([[battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, m_dep, mobile_wt, n_cores, pc, px_height, px_width, ram, sc_h, sc_w, talk_time, three_g, touch_screen, wifi]
])
        output=round(price[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this Mobile")
        else:
            return render_template('index.html',prediction_text="Estimated Range is {}".format(price))
    else:
        return render_template('index.html')
    

if __name__ == "__main__":
    app.run(debug = True)