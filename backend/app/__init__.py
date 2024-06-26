from flask import Flask
from flask_cors import CORS 

# Initialize web app.
app = Flask(__name__)
CORS(app)

from app import routes

