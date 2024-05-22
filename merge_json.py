import os
import json

def merge_json_files(output_file):
    json_list = []
    current_directory = os.path.dirname(os.path.abspath(__file__))

    for filename in os.listdir(current_directory):
        if filename.endswith('.json') and filename != output_file:
            filepath = os.path.join(current_directory, filename)
            with open(filepath, 'r') as file:
                data = json.load(file)
                json_list.append(data)

    merged_json = {"CustomThemes": json_list}

    with open(output_file, 'w') as outfile:
        json.dump(merged_json, outfile, indent=4)

if __name__ == "__main__":
    output_file = 'merged.json'

    merge_json_files(output_file)
    print("Successfully created merged json file!")
