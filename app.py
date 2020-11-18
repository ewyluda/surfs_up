# import flask dependency
from flask import Flask

# create a new flask app instance
app = Flask(__name__)

# create flask routines
@app.route('/')
def hello_world():
    return 'hello world'
