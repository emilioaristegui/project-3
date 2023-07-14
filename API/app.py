# Import the dependencies.
import pandas as pd
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, render_template
import json


#################################################
# Database Setup
#################################################

# Create database connection
connection_string= 'postgresql+psycopg2://postgres:1102@localhost:5433/Data'
engine = create_engine(connection_string)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# welcome route
@app.route('/')
def welcome():
    return render_template('index.html')

# pd.readsql route
@app.route('/data')
def return_data(): 
    
    results = pd.read_sql('select * from merged', engine)
    results = {
        'country': results['country'].to_list(),
        'region': results['region'].to_list(),
    }
    return results

# dataframe to json
#@app.route('/json')
#def return_json():
#df2 = results.to_json(orient = 'index')
#return df2

if __name__ == '__main__':
    app.run(debug=False)


