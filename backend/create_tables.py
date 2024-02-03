from app import create_app, db
from app.models.models import *  

app = create_app()
print("Creating tables...")
with app.app_context():
    db.create_all()
print("Tables created successfully.")

