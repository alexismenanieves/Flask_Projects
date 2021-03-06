# Section 0. Load libraries and custom functions --------------------------
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Section 1. Initialize Flask app -----------------------------------------
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__name__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' \
    + os.path.join(basedir, 'gapminder.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Section 2. Data Classes -------------------------------------------------
class Surveys(db.Model):
  __tablename__ = 'surveys'
  id = db.Column(db.Integer, primary_key=True)
  country = db.Column(db.String)
  year = db.Column(db.Integer)
  lifeExp = db.Column(db.Float)
  pop = db.Column(db.Integer)
  gdpPercap = db.Column(db.Float)

# Section 3. Serializations -----------------------------------------------
class SurveySchema(ma.Schema):
  class Meta:
    fields = ('lifeExp','pop','gdpPercap')
    
survey_schema = SurveySchema()

# Section 4. Routes -------------------------------------------------------
@app.route('/')
def open_home():
  return render_template('index.html')

@app.route('/<string:country>/<int:year>')
def show_survey(country: str, year: int):
  survey_values = Surveys.query.filter_by(country=country, year=year).first()
  result = survey_schema.dump(survey_values)
  return jsonify(result)

# Section 5. Main and App settings ----------------------------------------
if __name__ == '__main__':
  app.run(debug=True, host='127.0.0.1', port=5000)
