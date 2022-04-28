# Section 0. Load libraries and custom functions --------------------------
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Section 1. Initialize Flask app -----------------------------------------
app = Flask(__name__)

# Section 2. Data Classes -------------------------------------------------
basedir = os.path.abspath(os.path.dirname(__name__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite///' \
    + os.path.join(basedir,'gapminder.sqlite') 

# Section 3. Serializations -----------------------------------------------

# Section 4. Routes -------------------------------------------------------

# Section 5. Main and App settings ----------------------------------------
if __name__ == '__main__':
  app.run(debug=True, host='127.0.0.1', port=5000)
