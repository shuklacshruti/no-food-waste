from flask import Flask, send_from_directory
import os
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/kiannahendricks/Documents/NCAT/Graduate/Extracurriculars/Black Wings Hacks/food-waste/backend/yourdatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional: to suppress a warning
db = SQLAlchemy(app)

# Import and register your API blueprint after db initialization to avoid circular imports
from app.api.routes import api  # Update the import path based on your project structure
app.register_blueprint(api, url_prefix='/api')

# Serve React Frontend
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables for your models
    app.run(debug=True)  # Consider running in debug mode for development
