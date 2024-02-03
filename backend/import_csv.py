import argparse
import pandas as pd
from app import create_app, db
from app.models import FoodItem, Restaurant, Shelter

def import_restaurants(csv_path):
    df = pd.read_csv(csv_path)
    name_to_id = {}
    for _, row in df.iterrows():
        restaurant = Restaurant(name=row['name'], location=row['location'], contact_info=row['contact_info'])
        db.session.add(restaurant)
    db.session.commit()
    # Build a mapping of restaurant names to their IDs
    for restaurant in Restaurant.query.all():
        name_to_id[restaurant.name] = restaurant.id
    return name_to_id

def import_food_items(csv_path):
    df = pd.read_csv(csv_path)
    for _, row in df.iterrows():
        restaurant_id = row['restaurant_id']
        record = FoodItem(type=row['type'], quantity=row['quantity'], location=row['location'], restaurant_id=restaurant_id)
        db.session.add(record)
    db.session.commit()


def import_shelters(csv_path):
    df = pd.read_csv(csv_path)
    for _, row in df.iterrows():
        record = Shelter(name=row['name'], location=row['location'], contact_info=row['contact_info'])
        db.session.add(record)
    db.session.commit()

if __name__ == '__main__':
    app = create_app()
    app.app_context().push()

    parser = argparse.ArgumentParser(description='Import CSV data into the database.')
    parser.add_argument('csv_path', type=str, help='Path to the CSV file.')
    parser.add_argument('model_name', type=str, choices=['FoodItem', 'Restaurant', 'Shelter'], help='Model name to import data into.')
    args = parser.parse_args()

    # Import restaurants first and store their IDs
    if args.model_name == 'Restaurant':
        import_restaurants(args.csv_path)
    elif args.model_name == 'FoodItem':
        restaurant_mapping = {restaurant.name: restaurant.id for restaurant in Restaurant.query.all()}
        import_food_items(args.csv_path, restaurant_mapping)
    elif args.model_name == 'Shelter':
        import_shelters(args.csv_path)
