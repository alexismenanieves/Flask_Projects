from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/hello')
def hello_visitor():
  return jsonify(message = 'Hello visitor!')

@app.route('/')
def show_home():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True, host='127.0.0.1', port=5000)
