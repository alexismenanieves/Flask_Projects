from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_flask():
  return jsonify(message = 'Hello Flask')

@app.route('/parameters')
def get_parameters():
  # Now when we pass some parameters, we need the get method in request
  name = request.args.get('name')
  age = int(request.args.get('age'))
  if age < 18:
    # Now we have HTTP response status codes
    # 401 means that client request was not completed 'cause it's unauthorized
    return jsonify(message = 'Sorry ' + name + ', you are not authorized'), 401
  else:
    # 200 means OK, the request has succeded. 
    # For GET it means the resource has been fetched and it went to message body 
    return jsonify(mesage = 'Welcome ' + name), 200
  
if __name__ == '__main__':
  # Now we can run using debug to understand where we fail
  # And we can define here the host and port we want to use
  app.run(debug=True, host='127.0.0.1', port=5000)
  
# We can test this API using our browser or POSTMAN. The later is a great tool
# It's interesting to see the server is Werkzeug/2.0.3 Python/3.8.13

# REFERENCES
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200
