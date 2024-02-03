from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# entry point for Flask