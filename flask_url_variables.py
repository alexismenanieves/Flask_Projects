from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/url_variables/<string:name>/<int:age>')
