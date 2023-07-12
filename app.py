# Import the dependencies.
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template


#################################################
# Database Setup
#################################################

# create engine to hawaii.sqlite
engine = sqlalchemy.create_engine('postgresql:///data/db.db')
# reflect an existing database into a new model

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route('/data')
def return_data(): 
    results=engine.execute('select * from data').fetchall()
    #co2=[]
    #for each_result in results: 
     #   collision = dict(each_result)
      #  co2.append(collision)
    #return jsonify(co2)


@app.route('/')
def welcome():
    return render_template('index.html')
    #return(
        #f"Weclome to the CO2 Global Pollution API!<br/>"
        #f"<br/>"
        #f"Please find below all the available Routes:<br/>"
    #)

if __name__ == '__main__':
    app.run(debug=False)