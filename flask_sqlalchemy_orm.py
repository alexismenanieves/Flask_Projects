from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' \
    + os.path.join(basedir, 'gapminder.sqlite')
# See reference 1. Tracking modifications adds overhead, better deactivate 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def show_home():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True, host='127.0.0.1', port=5000)

# REFERENCES
# 1. About Track modifications: https://stackoverflow.com/questions/61573598/

