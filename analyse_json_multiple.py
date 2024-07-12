import os
import json

# Prompt the user for the directory containing JSON files and the name of the output file.

json_directory = input("Enter the path to the directory containing JSON files: ").strip()
output_file = input("Enter the name of the output file (e.g., 'results.txt'): ").strip()

# Define the list of scores to extract from the JSON files.
scores_of_interest = ['ics', 'ips', 'irmsd', 'tm_score', 'dockq']

if not os.path.isdir(json_directory):
    print(f"Error: The directory '{json_directory}' does not exist.")
    exit(1)

# Open the output file for writing. This file will store the extracted scores.
with open(output_file, 'w') as output:
    for json_file in os.listdir(json_directory):
        if json_file.endswith('.json'):
            
            json_path = os.path.join(json_directory, json_file)
            with open(json_path) as f:
                data = json.load(f)
                
                # Extract the scores of interest
                extracted_scores = {score_name: data.get(score_name) for score_name in scores_of_interest}
                
                # Write the name of the JSON file being processed to the output file.
                output.write(f"File: {json_file}\n")
                
                # Write each extracted score and its value (or `None`) to the output file.
                for score_name, score_value in extracted_scores.items():
                    output.write(f"{score_name}: {score_value}\n")
                output.write("\n")  

# Little print
print(f"Scores successfully written to {output_file}")
