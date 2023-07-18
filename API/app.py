# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
#from sqlalchemy.ext.automap import automap_base
#from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, render_template
import json
#import plotly.express as px



#################################################
# Database Setup
#################################################

# Create database connection

#connection_string= 'postgresql+psycopg2://postgres:1102@localhost:5433/Data'
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
@app.route('/data_emissions')
def return_data(): 
    
    #reading SQL database, creating a pandas df for easier manipulation
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
    #pandas df converted into json file
    df = df.groupby("region")["emissions"].sum()
    df = df.to_json(orient="split")
    return df

@app.route('/country_emissions')
def country_emissions(): 
    
    #reading SQL database, creating a pandas df for easier manipulation
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
    #pandas df converted into json file
    df = df.groupby("country")["emissions"].sum()
    df = df.to_json(orient="split")
    return df

@app.route('/industry_emissions')
def industry_emissions(): 
    
    #reading SQL database, creating a pandas df for easier manipulation
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
    #pandas df converted into json file
    df = df.groupby("industry")["emissions"].sum()
    df = df.to_json(orient="split")
    return df

if __name__ == '__main__':
    app.run(debug=False)