from app.extensions import db

# Association Table
shelter_food_item_association = db.Table('shelter_food_item_association',
    db.Column('shelter_id', db.Integer, db.ForeignKey('shelter.id'), primary_key=True),
    db.Column('food_item_id', db.Integer, db.ForeignKey('food_item.id'), primary_key=True)
)


class FoodItem(db.Model):
    __tablename__ = 'food_item'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(128), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(128), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))  # Add this line
    restaurant = db.relationship('Restaurant', back_populates='food_items')
class Restaurant(db.Model):
    _tablename__ = 'restaurant'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    location = db.Column(db.String(128), nullable=False)
    contact_info = db.Column(db.String(128))
    food_items = db.relationship('FoodItem', back_populates='restaurant')
class Shelter(db.Model):
    __tablename__ = 'shelter'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    location = db.Column(db.String(128), nullable=False)
    contact_info = db.Column(db.String(128))
    interested_food_items = db.relationship('FoodItem', secondary=shelter_food_item_association, backref=db.backref('interested_shelters', lazy='dynamic'))
