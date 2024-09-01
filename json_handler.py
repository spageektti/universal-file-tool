import json
import os
import csv

def read_json(file_path):
    """Read and print the contents of a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            print(json.dumps(data, indent=4))  # Pretty print the JSON data
    except Exception as e:
        print(f"Error reading JSON file: {e}")

def write_json(file_path):
    """Write data to a new JSON file."""
    try:
        data = input("Enter JSON data to write (as a valid JSON string): ")
        json_data = json.loads(data)  # Convert string to JSON object
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4)
        print(f"Data written to JSON successfully: {file_path}")
    except Exception as e:
        print(f"Error writing to JSON file: {e}")

def append_to_json(file_path):
    """Append data to an existing JSON file."""
    try:
        with open(file_path, 'r+', encoding='utf-8') as json_file:
            data = json.load(json_file)
            new_data = input("Enter new data to append (as a valid JSON string): ")
            new_data = json.loads(new_data)
            if isinstance(data, list):
                data.append(new_data) 
            elif isinstance(data, dict):
                data.update(new_data)
            else:
                print("Unsupported JSON structure for appending.")
                return
            json_file.seek(0)  
            json.dump(data, json_file, indent=4)
            json_file.truncate() 
        print(f"Data appended to JSON successfully: {file_path}")
    except Exception as e:
        print(f"Error appending to JSON file: {e}")

def convert_json_to_csv(file_path):
    """Convert a JSON file to CSV format."""
    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            if isinstance(data, list):
                csv_file_path = os.path.splitext(file_path)[0] + ".csv"
                with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
                    writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
                    writer.writeheader()
                    writer.writerows(data)
                print(f"JSON converted to CSV successfully: {csv_file_path}")
            else:
                print("JSON data is not in a list format, cannot convert to CSV.")
    except Exception as e:
        print(f"Error converting JSON to CSV: {e}")

def pretty_print_json(file_path):
    """Pretty print the contents of a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            print(json.dumps(data, indent=4)) 
    except Exception as e:
        print(f"Error reading JSON file for pretty print: {e}")

def merge_json_files(file_paths):
    """Merge multiple JSON files into a single JSON file."""
    merged_data = []
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                if isinstance(data, list):
                    merged_data.extend(data)
                else:
                    print(f"Warning: {file_path} does not contain a list. Skipping.")
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    
    if merged_data:
        output_file_path = "merged_output.json"
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            json.dump(merged_data, output_file, indent=4)
        print(f"Merged JSON data written to: {output_file_path}")

def handle_json(file_path):
    """Handle JSON file operations."""
    print("1. Read JSON")
    print("2. Write to JSON")
    print("3. Append to JSON")
    print("4. Convert JSON to CSV")
    print("5. Pretty Print JSON")
    print("6. Merge JSON Files")
    choice = input("Select option: ")
    if choice == "1":
        read_json(file_path)
    elif choice == "2":
        write_json(file_path)
    elif choice == "3":
        append_to_json(file_path)
    elif choice == "4":
        convert_json_to_csv(file_path)
    elif choice == "5":
        pretty_print_json(file_path)
    elif choice == "6":
        num_files = int(input("How many JSON files do you want to merge? "))
        file_paths = [input(f"Enter path for JSON file {i + 1}: ") for i in range(num_files)]
        merge_json_files(file_paths)
    else:
        print("Invalid option selected.")
