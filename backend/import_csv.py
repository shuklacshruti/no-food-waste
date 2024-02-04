import pandas as pd
import argparse
from app import create_app, db
from app.models import FoodItem  # Ensure this is the corrected model import

def import_data(csv_path):
    df = pd.read_csv(csv_path)
    for _, row in df.iterrows():
        # Assuming your CSV columns are named appropriately
        food_item = FoodItem(
            type=row['restaurant_food_type'],
            quantity=row['quantity'],  # Ensure quantity is handled correctly; might need adjustment based on CSV structure
            location=row['restaurant_location'],
            source='Restaurant',  # This assumes all entries are restaurants; adjust if shelters are also included
            source_name=row['restaurant_name']
        )
        db.session.add(food_item)
    db.session.commit()

if __name__ == '__main__':
    app = create_app()
    app.app_context().push()

    parser = argparse.ArgumentParser(description='Import CSV data into the database.')
    parser.add_argument('csv_path', type=str, help='Path to the CSV file.')
    args = parser.parse_args()

    import_data(args.csv_path)
