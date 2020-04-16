from flask import Flask, jsonify, render_template
from bs4 import BeautifulSoup as bs
import requests
import operator

import time
import pandas as pd
import datetime as dt
# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo
from config import dbkey

# conn2 = f"mongodb://heroku_app:{dbkey}@dwelling-db-shard-00-00-yfzol.gcp.mongodb.net:27017,dwelling-db-shard-00-01-yfzol.gcp.mongodb.net:27017,dwelling-db-shard-00-02-yfzol.gcp.mongodb.net:27017/test?ssl=true&replicaSet=dwelling-db-shard-0&authSource=admin&retryWrites=true&w=majority"
conn2 = f"mongodb://heroku_app:{dbkey}@dwelling-db-shard-00-00-yfzol.gcp.mongodb.net:27017,dwelling-db-shard-00-01-yfzol.gcp.mongodb.net:27017,dwelling-db-shard-00-02-yfzol.gcp.mongodb.net:27017/test?ssl=true&replicaSet=dwelling-db-shard-0&authSource=admin&retryWrites=true&w=majority"

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/rr")
def railroad():
    # Create connection variable
    # conn2 = 'mongodb://localhost:27017'
    listings = []
    # Pass connection to the pymongo instance.
    client2 = pymongo.MongoClient(conn2)

    # Connect to a database. Will create one if not already available.
    db2 = client2.Dwelling_db
    listings = [doc for doc in db2.Rail_stops.find({}, {'_id':False})]

    return jsonify(listings)


@app.route("/hs")
def highSchool():
    # Create connection variable
    # conn2 = 'mongodb://localhost:27017'
    schools = []

    # Pass connection to the pymongo instance.
    client2 = pymongo.MongoClient(conn2)

    # Connect to a database. Will create one if not already available.
    db2 = client2.Dwelling_db
    
    schools = [doc for doc in db2.high_school2019.find({}, {'_id':False})]
    
    return jsonify(schools)

@app.route("/heat")
def heat():
    # Create connection variable
    # conn2 = 'mongodb://localhost:27017'
    munis = []

    # Pass connection to the pymongo instance.
    client2 = pymongo.MongoClient(conn2)

    # Connect to a database. Will create one if not already available.
    db2 = client2.Dwelling_db
    
    munis = [doc for doc in db2.HeatSource.find({}, {'_id':False})]
    
    return jsonify(munis)

@app.route("/hs/<muni>")
def highSchoolMarkers(muni):
    # Create connection variable
    # conn2 = 'mongodb://localhost:27017'
    schools = []

    # Pass connection to the pymongo instance.
    client2 = pymongo.MongoClient(conn2)

    # Connect to a database. Will create one if not already available.
    db2 = client2.Dwelling_db
    
    schools = [doc for doc in db2.high_school2019.find({"Municipal ID": int(muni)}, {'_id':False})]
    
    return jsonify(schools)

# @app.route("/bstop")
# def busStops():
#     # Create connection variable
#     # conn2 = 'mongodb://localhost:27017'
#     busStops = []

#     # Pass connection to the pymongo instance.
#     client2 = pymongo.MongoClient(conn2)

#     # Connect to a database. Will create one if not already available.
#     db2 = client2.Dwelling_db
#     busStops = [doc for doc in db2.Bus_stops.find({}, {'_id':False})]

#     return jsonify(busStops)


@app.route("/bs/<muni>")
def busStopsCity(muni):
# @app.route("/bs")
# def busStopsCity():
    busStops = []

    # Pass connection to the pymongo instance.
    client2 = pymongo.MongoClient(conn2)
    # Connect to a database. Will create one if not already available.
    db2 = client2.Dwelling_db
    busStops = [doc for doc in db2.Bus_stops.find({"MUNID": int(muni)}, {'_id':False})]
    # busStops = [doc for doc in db2.Bus_stops.find({}, {'_id':False})]
    
    return jsonify(busStops)


# @app.route("/rrs/<muniID>")
@app.route("/rrs/<muni>")
def trainStopsCity(muni):
    # Create connection variable
    trainStops = []

    # Pass connection to the pymongo instance.
    client2 = pymongo.MongoClient(conn2)
    # search = str(mID)
    # Connect to a database. Will create one if not already available.
    db2 = client2.Dwelling_db
    trainStops = [doc for doc in db2.Rail_stops.find({"Muni Code": int(muni)}, {'_id':False})]
    # trainStops = [doc for doc in db2.Rail_stops.find({}, {'_id':False})]
 
    return jsonify(trainStops)

@app.route("/walkScore")
def walkScores():
    # Create connection variable
    # conn2 = 'mongodb://localhost:27017'
    listings = []

    # Pass connection to the pymongo instance.
    client2 = pymongo.MongoClient(conn2)

    # Connect to a database. Will create one if not already available.
    db2 = client2.Dwelling_db
    walkScores = [doc for doc in db2.WalkScore.find({}, {'_id':False})] 
    
    return jsonify(walkScores)

@app.route("/actScore")
def actScores():
    # Create connection variable
    # conn2 = 'mongodb://localhost:27017'
    actScore = []

    # Pass connection to the pymongo instance.
    client2 = pymongo.MongoClient(conn2)

    # Connect to a database. Will create one if not already available.
    db2 = client2.Dwelling_db
    actScore = [doc for doc in db2.ActivityScore.find({}, {'_id':False})] 
    
    return jsonify(actScore)

@app.route("/crimeScore")
def crimeScores():
    # Create connection variable
    # conn2 = 'mongodb://localhost:27017'
    crimeScore = []

    # Pass connection to the pymongo instance.
    client2 = pymongo.MongoClient(conn2)

    # Connect to a database. Will create one if not already available.
    db2 = client2.Dwelling_db
    crimeScore = [doc for doc in db2.CrimeScore.find({}, {'_id':False})] 
    
    return jsonify(crimeScore)

@app.route("/eduScore")
def eduScores():
    # Create connection variable
    # conn2 = 'mongodb://localhost:27017'
    eduScore = []

    # Pass connection to the pymongo instance.
    client2 = pymongo.MongoClient(conn2)

    # Connect to a database. Will create one if not already available.
    db2 = client2.Dwelling_db
    eduScore = [doc for doc in db2.EduScore.find({}, {'_id':False})] 
    
    return jsonify(eduScore)


if __name__ == "__main__":
    app.run(debug=True)
