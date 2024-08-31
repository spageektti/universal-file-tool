import csv
import json
import os

def read_csv(file_path):
    """Read and print the contents of a CSV file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                print(row)
    except Exception as e:
        print(f"Error reading CSV file: {e}")

def write_csv(file_path):
    """Write data to a new CSV file."""
    try:
        data = input("Enter data to write to CSV (comma-separated): ")
        with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data.split(','))
        print(f"Data written to CSV successfully: {file_path}")
    except Exception as e:
        print(f"Error writing to CSV file: {e}")

def append_to_csv(file_path):
    """Append data to an existing CSV file."""
    try:
        data = input("Enter data to append to CSV (comma-separated): ")
        with open(file_path, 'a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data.split(','))
        print(f"Data appended to CSV successfully: {file_path}")
    except Exception as e:
        print(f"Error appending to CSV file: {e}")

def convert_csv_to_json(file_path):
    """Convert a CSV file to JSON format."""
    try:
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            json_data = [row for row in reader]
        json_file_path = os.path.splitext(file_path)[0] + ".json"
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4)
        print(f"CSV converted to JSON successfully: {json_file_path}")
    except Exception as e:
        print(f"Error converting CSV to JSON: {e}")

def filter_csv(file_path):
    """Filter rows in a CSV file based on a condition."""
    try:
        condition = input("Enter a condition to filter rows (e.g., column_name=value): ")
        column_name, value = condition.split('=')
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            filtered_rows = [row for row in reader if row.get(column_name) == value]
        for row in filtered_rows:
            print(row)
    except Exception as e:
        print(f"Error filtering CSV file: {e}")

def handle_csv(file_path):
    """Handle CSV file operations."""
    print("1. Read CSV")
    print("2. Write to CSV")
    print("3. Append to CSV")
    print("4. Convert CSV to JSON")
    print("5. Filter CSV")
    choice = input("Select option: ")
    if choice == "1":
        read_csv(file_path)
    elif choice == "2":
        write_csv(file_path)
    elif choice == "3":
        append_to_csv(file_path)
    elif choice == "4":
        convert_csv_to_json(file_path) 
    elif choice == "5":
        filter_csv(file_path)
    else:
        print("Invalid option selected.")
