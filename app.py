from cmath import atan
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


engine = create_engine("sqlite:////Users/alexisbloor/Desktop/Homework/sqlalchemy-challenge/Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

measurements = Base.classes.measurement
stations = Base.classes.station

app= Flask(__name__)

# Flask routes
@app.route("/")
def welcome():
    return (
        f"Climate API"
        f"Available Routes"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
    )
    
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    result = session.query(measurements.date, measurements.prcp).all()
    session.close()

    prcp_data = []
    for result in results:
        prcp_dict = {}
        prcp_dict["date"] = result[0]
        prcp_dict["prcp"] = result[1]
        prcp_data.append(prcp_dict)
    return jsonify(prcp_data)


@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(stations.station, stations.name, stations.latitude, stations.longitude, stations.elevation).all()
    session.close()

    all_stations = []
    for result in results:
        station_dict = {}
        station_dict["station"] = result[0]
        all_stations.append(station_dict)
        return jsonify(all_stations)