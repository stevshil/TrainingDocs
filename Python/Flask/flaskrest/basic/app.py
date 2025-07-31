from flask import Flask, jsonify
from flask_restful import Resource, Api
import mysql.connector

app = Flask("api")
api = Api(app)

people = [
    {'name': 'Steve',
     'subject': 'Linux'},
    {"name": "Fridah",
     "subject": "Java"},
    {"name": "Jack",
     "subject": "Python"}
]

# Global database connection for the service lifetime
def dbconn():
    try: 
        global sakila
        sakila = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "secret123",
            database = "pubs"
        )
        print(sakila)
    except Exception as e:
        print(f"Error connecting to database {e}")

# restful api method of getting data
class getActors(Resource):
    # Adding the default get method
    def get(self):
        sakcursor = sakila.cursor(dictionary=True)
        sakcursor.execute("SELECT * FROM authors")
        authors = sakcursor.fetchall()
        sakcursor.close()
        return jsonify(authors)

# Basic app.route method to get data    
def getActorsBasic():
    sakcursor = sakila.cursor(dictionary=True)
    sakcursor.execute("SELECT * FROM authors")
    authors = sakcursor.fetchall()
    sakcursor.close()
    return jsonify(authors)

@app.route("/users")
def getusers():
    # Made a call to the database. using SELECT
    # return jsonify(("Jack","Fridah","Steve"))
    return jsonify(people)

@app.route("/actors")
def getallactors():
    mydata = getActorsBasic()
    return mydata

api.add_resource(getActors, '/api/actors')

if __name__ == "__main__":
    dbconn()
    try:
        app.run(debug=True, host="0.0.0.0")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the database connection when the application terminates
        sakila.close()