# csv_utils.py
import csv

def load_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None