# Section 0. Import libraries ---------------------------------------------

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, Float
from flask_marshmallow import Marshmallow
import os

# Section 1. Initialize Flask app -----------------------------------------

app = Flask(__name__)
# We'll use now the Gapminder database. To retrieve it we'll need
# to define the path to the file using 'os' library and our engine
# will be sqlite
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' \
    + os.path.join(basedir, 'gapminder.sqlite')
# See reference 1. Tracking modifications adds overhead, better deactivate 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# Always initialize db then marshmallow. See reference 5
ma = Marshmallow(app)

# Section 2. Data Classes -------------------------------------------------

class Surveys(db.Model):
  __tablename__ = 'surveys'
  id = db.Column(db.Integer, primary_key = True)
  country = db.Column(db.String)
  year = db.Column(db.Integer)
  lifeExp = db.Column(db.Float)
  pop = db.Column(db.Integer)
  gdpPercap = db.Column(db.Float)
  
# Section 3. Routes -------------------------------------------------------

@app.route('/')
def show_home():
  return render_template('index.html')

@app.route('/peru_2007', methods = ['GET'])
def peru_2007():
  peru_2007_stats = Surveys.query.filter_by(country='Peru', year=2007).first()
  # Now this process is called serialization
  result = peru_schema.dump(peru_2007_stats)
  return jsonify(result)
  
# Section 4. Serializations -----------------------------------------------

class PeruSchema(ma.Schema):
  class Meta:
    # Here we select the fields we want to show
    fields = ('lifeExp','pop','gdpPercap')

peru_schema = PeruSchema()

# Section 5. Main and App settings ----------------------------------------
if __name__ == '__main__':
  app.run(debug=True, host='127.0.0.1', port=5000)
  
# NOTES
# a. I received some warnings about Flask-SQLAlchemy integration that requires 
# marshmallow-sqlalchemy to be installed. So I did that using:
# conda install -c conda-forge marshmallow-sqlalchemy
# b. This is a great learning moment. I received an error telling me that 
# "Mapper mapped class Surveys->surveys could not assemble any primary key 
# columns for mapped table 'surveys'" and according to ref. 2 you always need 
# in a DB a key when creating an object. So you have to modyfy the table to 
# have a key but it seems that you can't do it directly in SQLite, based on 
# ref. 3. The recipe is to rename the table (to old), create a new table with 
# the old structure and the id, then pass all data from old table to new, then
# drop the old table. It is important to call foreign_keys=off with PRAGMA at
# the start and at foreign keys=on at the end 
# c. Do I have to worry about autoincrement in an id? No, it seems that it 
# imposes extra CPU resources, let the id as primary and sqlite will create 
# it's increments alone, according to ref 4.
# d. Serialization is the process of converting an object into a textual 
# representation. The inverted process is called deserialization

# REFERENCES
# 1. About Track modifications: https://stackoverflow.com/questions/61573598/
# 2. On needing db key in Flask: https://stackoverflow.com/questions/24872541/
# 3. Recipe to add a db key: https://www.sqlitetutorial.net/sqlite-primary-key/
# 4. About autoincrement: https://sqlite.org/autoinc.html
# 5. Sequence marshmallow: https://flask-marshmallow.readthedocs.io/en/latest/

