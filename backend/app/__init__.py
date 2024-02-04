from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .extensions import db
from flask_cors import CORS
from .api.routes import api as api_blueprint

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/kiannahendricks/Documents/NCAT/Graduate/Extracurriculars/Black Wings Hacks/food-waste/backend/yourdatabase.db'
    db.init_app(app)

    # Import your database models here
    from .models.models import FoodItem

    # Register the Blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
