import os
import pprint
from flask_pymongo import PyMongo
from flask import Flask, jsonify, request,render_template
from bson import json_util, ObjectId
import json
import pymongo

# Debugging variables
flask_debugging = True  # Set to True when in Flask debug mode (DISABLE BEFORE DEPLOYING LIVE)

# Initialize Flask
app = Flask(__name__)
mongo = PyMongo(app)
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.comboPlantsDB
#collection = db.myCollection

#MONGODB_URI = os.environ.get('MONGODB_URI')
#if not MONGODB_URI:
 #   MONGODB_URI = "mongodb://localhost:27017/comboPlantsDB"

#app.config['MONGO_URI'] = MONGODB_URI


@app.route("/")
def index():
    """Return the homepage."""
    return render_template('index.html')

@app.route('/test/<abc>')
def getTest(abc):
    mess = 'This works'+ abc
    return jsonify(mess)    


# Route that outputs database results
@app.route('/families/<family>')
def getData(family):
    """ Retrieve & return all species records for a family from the MongoDB collection 
        Returns: jsonified results """

    results = db.myCollection.find({'family':family})
    familyList = []
    for result in results:
        try:
            familyList.append([result['id'], result['scientificName'],result['decimalLatitude'],\
            result['decimalLongitude'],result['habitat'],result['eventDate'],result['identifiedBy'],\
            result['recordedBy'], result['county'], result['accessURI'], result['thumbnailAccessURI']])
        except:
            continue 
          
    #db = comboPlantsDB
     
    #results = db.myCollection.find({'family':family})
    #familyList = []
    #for result in results:
     #   try:
      #      familyList.append([result['id'], result['scientificName'],result['decimalLatitude'],\
      #      result['decimalLongitude'],result['habitat'],result['eventDate'],result['identifiedBy'],\
       #     result['recordedBy'], result['county'], result['accessURI'], result['thumbnailAccessURI']])
        #except:
         #   continue    
    return jsonify(familyList)


#
# *** Main script execution ***
#
if __name__ == "__main__":
    app.run(debug=flask_debugging)
 