from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, Float
from flask_marshmallow import Marshmallow
import os

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

# Section 1. Data Classes -------------------------------------------------

class Surveys(db.Model):
  __tablename__ = 'surveys'
  country = Column(String)
  year = Column(Integer)
  lifeExp = Column(Float)
  pop = Column(Integer)
  gdpPercap = Column(Float)
  
# Section 2. Routes -------------------------------------------------------

@app.route('/')
def show_home():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True, host='127.0.0.1', port=5000)

# REFERENCES
# 1. About Track modifications: https://stackoverflow.com/questions/61573598/

