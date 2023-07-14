# Import the dependencies.
import numpy as np
import pandas as pd
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

#connection_string= 'postgresql+psycopg2://postgres:1102@localhost:5433/Data'
connection_string= 'postgresql+psycopg2://postgres:1234@localhost:5432/project_3'
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
        'emissions': results['emissions'].to_list(),
        'industry': results['industry'].to_list(),
        'segment': results['segment'].to_list(),
        'reason': results['reason'].to_list(),
        'baseYear': results['base_year'].to_list(),
        'ISO': results['iso_3166_country_code'].to_list(),
        'Lat': results['latitude'].to_list(),
        'Lon': results['longitude'].to_list(),
        
    }
    df = pd.DataFrame(results, columns = ['region', 'country','emissions','industry','segment','reason','baseYear','ISO','Lat','Lon'])
    df.to_json('static/merged.json')
    return results

if __name__ == '__main__':
    app.run(debug=False)



