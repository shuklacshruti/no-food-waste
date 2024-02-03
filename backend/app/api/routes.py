from flask import Blueprint, jsonify, request
from app.services.match_service import find_matches
from .. import db
from app.models.models import FoodItem, Restaurant

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

# backend/app/api/routes.py

@api.route('/find_matches', methods=['GET'])
def get_find_matches():
    item_type = request.args.get('type', default="")
    item_location = request.args.get('location', default="")
    
    # Call the find_matches function to get the matches
    matches = find_matches(item_type, item_location)

    return jsonify([
        {
            'id': match['id'],
            'type': match['type'],
            'location': match['location'],
            'restaurantName': match['restaurantName']  # Use the correct attribute name
        } for match in matches
    ])




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