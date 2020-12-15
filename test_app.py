import flask
from flask import request, jsonify
from flask_cors import CORS
import json

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive old version</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''
