from flask import Flask, jsonify, render_template, request
from joblib import load
import pandas as pd
import numpy as np
import time
app = Flask(__name__)
rf=load('model')
#app.debug = True
@app.route('/',methods = ['GET','POST'])
def index():
        if request.method == 'POST': # basic Flask structure 
                carrier = request.form['carrier'] 
                origin =request.form['origin']
                dest=request.form['dest']
                temp =request.form['temp']
                humid=request.form['humid']
                year =request.form['year']
                month =request.form['month']
                day   =request.form['day']
                time  =request.form['time']
                fin=[int(year),int(month),int(day),int(time),carrier,origin,dest,float(temp),float(humid)]
                flag=pd.DataFrame([fin],columns=["year","month","day","dep_time","carrier","origin","dest","temp","humid"])
                output=rf.predict(flag)
                if output[0] !=-1:
                        return render_template('output.html', delay=output[0])
        return render_template('index.html')

@app.errorhandler(500)
def not_found(e):
        return render_template('error.html'), 500

if __name__=='__main__':
    app.run()