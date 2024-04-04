import json
import yaml

def check_json_syntax(file_path):
    try:
        with open(file_path, 'r') as file:
            json.load(file)
        print(f"{file_path} has valid JSON syntax.")
    except json.JSONDecodeError as e:
        print(f"Error in {file_path}: Invalid JSON syntax.")
        print(e)

def check_yaml_syntax(file_path):
    try:
        with open(file_path, 'r') as file:
            yaml.safe_load(file)
        print(f"{file_path} has valid YAML syntax.")
    except yaml.YAMLError as e:
        print(f"Error in {file_path}: Invalid YAML syntax.")
        print(e)

def main():
    file_path = input("Enter the file path: ")
    if file_path.endswith('.json'):
        check_json_syntax(file_path)
    elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
        check_yaml_syntax(file_path)
    else:
        print("Unsupported file format. Please provide a JSON or YAML file.")

if __name__ == "__main__":
    main()
