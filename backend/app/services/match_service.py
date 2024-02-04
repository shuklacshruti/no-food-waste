from app.extensions import db
from app.models.models import FoodItem

def find_matches(item_type, item_location):
    results = FoodItem.query.filter_by(
        type=item_type,
        location=item_location
    ).all()

    matches = [
        {
            "id": result.id,
            "type": result.type,
            "location": result.location,
            "sourceName": result.source_name  # Use source_name directly from FoodItem
        } for result in results
    ]
    return matches
