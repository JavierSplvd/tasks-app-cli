import csv


def create_database(csv_filename: str):
    try:
        with open(csv_filename, mode='w', newline='') as file:
            csv.writer(file)
        print("CSV created!")
    except Exception as e:
        print(f"An error occurred while creating the CSV: {str(e)}")