import flask
import requests
from flask_mysqldb import MySQL 
from flask import request, json, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.config['MYSQL_HOST'] = 'host.docker.internal'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORDS'] = ''
app.config['MYSQL_DB'] = 'flaskhost'

@app.route("/", methods=["GET"])
def index():
    response = requests.get('https://randomuser.me/api')  
    data = response.json() 
    return jsonify(data) 

@app.route("/inserthost", methods=["POST"])
def inserthost():
    data = request('https://randomuser.me/api')
    username = data['results'][0]['name']['first']

    cur = mysql.connection.cursor()
    cur.execute("""insert into user(name) values(%s)""", (username,))
    mysql.connection.commit()
    cur.close

if __name__ == "__main__":  
    app.run(host="0.0.0.0", debug=True, port=5000) 
