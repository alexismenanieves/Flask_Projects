# Now if we want to create a RESTful API, we return a JSON
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_flask_jsonify():
  # jsonify convert our message into a key a value pair JSON
  return jsonify(message='Hello Flask & jsonify!')

if __name__ == '__main__':
  app.run()
