# Section 0. Import libraries and custom functions
from flask import Flask, jsonify, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import json

# Section 1. Initialize Flask app -----------------------------------------
app = Flask(__name__)
# credentials
db_user = os.getenv('DBUSER')
db_pass = os.getenv('DBPASS')
db_name = os.getenv('DBNAME')
db_host = os.getenv('DBHOST')
db_port = os.getenv('DBPORT')

app.config["SQLALCHEMY_DATABASE_URI"] \
    = f"mysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Section 2. Data Classes -------------------------------------------------
class Artist(db.Model):
  __tablename__ = 'Artist'
  ArtistId = db.Column(db.Integer, primary_key=True)
  Name = db.Column(db.String)

# Section 3. Routes -------------------------------------------------------
@app.route('/')
def show_home():
  return render_template('index.html')
  
@app.route('/<int:Artistid>')
def show_artist(Artistid: int):
  my_query = Artist.query.filter_by(ArtistId=Artistid).first()
  my_result = artist_schema.dump(my_query)
  return jsonify(my_result)

# Section 4. Serializations -----------------------------------------------
class ArtistSchema(ma.Schema):
  class Meta:
    fields = ('ArtistId','Name')
    
artist_schema = ArtistSchema()

# Section 5. Main and App settings ----------------------------------------
if __name__ == '__main__':
  app.run(debug=True, host='127.0.0.1', port=5000)
  
# NOTES
# Some credentials should be protected, so we must call them using 
# environment variables. The way to create such variables in Unix and Mac is
# in the terminal, type the following command
# export DBUSER=value 
# And to retrieve the value you should use in Python
# os.getenv('DBUSER')
# alternatively, you can use environ.get, which returns None is not available
# os.environ.get('DBUSER')

# REFERENCES
# [1] twilio blog. Retrieved May 12, 2022. Working with Environment Variables 
# in Python. https://www.twilio.com/blog/environment-variables-python
  
