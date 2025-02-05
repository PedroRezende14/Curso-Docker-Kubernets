import flask
import requests 
from flask import request, json, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET"])
def index():
    response = requests.get('https://randomuser.me/api')  
    data = response.json() 
    return jsonify(data) 

if __name__ == "__main__":  
    app.run(host="0.0.0.0", debug=True, port=5000) 
