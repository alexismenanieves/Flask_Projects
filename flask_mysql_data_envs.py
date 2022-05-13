# Section 0. Import libraries and custom functions
from flask import Flask, jsonify, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import json

# Section 1. Initialize Flask app -----------------------------------------
app = Flask(__name__)
# credentials
db_user = 
db_pass = 
db_name = 
db_host = 
db_port = 

app.config["SQLALCHEMY_DATABASE_URI"] \
    = f"mysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Section 2. Data Classes -------------------------------------------------
class Artist(db.Model):
  __tablename__ = 'Artist'
  ArtistId = db.Column(db.Integer, primaryKey=True)
  Name = db.Column(db.String)
  
# Section 3. Routes -------------------------------------------------------
@app.route('/')
def show_home():
  return render_template('index.html')

@app.route('/<int:Artistid>')
def show_artist(Artistid: int):
  myquery = Artist.query.filter_by(Artistid=Artistid).first()
  myresult = artist_schema.dump(my_query)
  return jsonify(myresult)

# Section 4. Serializations -----------------------------------------------
