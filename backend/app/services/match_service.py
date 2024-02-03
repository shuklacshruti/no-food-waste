from app.extensions import db
from app.models.models import FoodItem, Restaurant

def find_matches(item_type, item_location):
    results = db.session.query(
        FoodItem.id,
        FoodItem.type,
        FoodItem.location,
        Restaurant.name.label("restaurantName")  # Updated label to match frontend
    ).join(
        Restaurant, FoodItem.restaurant_id == Restaurant.id
    ).filter(
        FoodItem.type == item_type,
        FoodItem.location == item_location
    ).all()

    matches = [
        {
            "id": result.id,
            "type": result.type,
            "location": result.location,
            "restaurantName": result.restaurantName
        } for result in results
    ]
    return matches

