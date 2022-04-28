from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def show_home():
  return render_template('index.html')

# You can pass variables as url strings
@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age: int):
  if age < 18:
    return jsonify(message = 'We are sorry ' + name + ' not authorized'), 401
  else:
    return jsonify(message = 'Welcome back ' + name), 200

if __name__ == '__main__':
  app.run(debug=True, host='127.0.0.1', port=5000)
