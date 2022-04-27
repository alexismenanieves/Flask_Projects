from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_flask_jsonify():
  return jsonify(message='Hello Flask & jsonify!')

if __name__ == '__main__':
  app.run()
