from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the Flask API!"
    
@app.route("/date")
def date():
    return "This page was served at " + str(datetime.now())
    
counter = 0
   
@app.route("/count_views")
def count_views():
    global counter
    counter += 1
    return "This page was served " + str(counter) + " times"
 
