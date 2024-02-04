from flask import Blueprint, jsonify, request
from app.services.match_service import find_matches
from .. import db
from app.models.models import FoodItem

api = Blueprint('api', __name__)

@api.route('/')
def home():
    return "Welcome to the Flask App!"

@api.route('/check_database')
def check_database():
    # Query a sample record from the database
    sample_data = FoodItem.query.first()
    if sample_data:
        return jsonify({'message': 'Database connection successful'})
    else:
        return jsonify({'message': 'Database connection failed'})

# backend/app/api/routes.py
from flask import Blueprint, jsonify, request
# Ensure your imports are correct, especially if you've moved the find_matches logic
from app.models.models import FoodItem  # Adjust this if the import path is incorrect

api = Blueprint('api', __name__)

@api.route('/find_matches', methods=['GET'])
def get_find_matches():
    item_type = request.args.get('type', default="")
    item_location = request.args.get('location', default="")

    # Query the FoodItem model directly based on the item_type and item_location
    matches = FoodItem.query.filter_by(type=item_type, location=item_location).all()

    # Prepare the data to be returned as JSON
    results = [
        {
            'id': match.id,
            'type': match.type,
            'location': match.location,
            'sourceName': match.source_name  # Use source_name to represent restaurant or shelter name
        } for match in matches
    ]

    return jsonify(results)





@api.route('/fooditems', methods=['POST'])
def add_food_item():
    data = request.get_json()
    new_food_item = FoodItem(
        type=data['type'],
        quantity=data['quantity'],
        location=data['location']
    )
    db.session.add(new_food_item)
    db.session.commit()
    return jsonify({'message': 'Food item added successfully!'}), 201