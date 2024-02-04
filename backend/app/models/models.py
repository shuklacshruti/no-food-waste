from app.extensions import db

class FoodItem(db.Model):
    __tablename__ = 'food_item'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(128), nullable=False)
    quantity = db.Column(db.Integer)  # Adjusted to allow for nullable if your CSV might have empty quantity values
    location = db.Column(db.String(128), nullable=False)
    source = db.Column(db.String(128), nullable=False)  # To differentiate between 'Shelter' and 'Restaurant'
    source_name = db.Column(db.String(128), nullable=False)  # The name of the shelter or restaurant

# Example records in the FoodItem table:
# 1, Vegetables, 10, New York, Restaurant, Good Eats
# 2, Bread, 5, Chicago, Restaurant, Bread Basket
# 3, Pizza, 8, Charlotte, Restaurant, Pizza Bob
# 4, Vegetables, 20, New York, Shelter, Hope Shelter
# 5, Bread, 15, Chicago, Shelter, Safe House
# 6, Pizza, 12, Charlotte, Shelter, Food for All
