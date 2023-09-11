import os
import csv
from collections import Counter

ELECTION_DATA_PATH = os.path.join('Resources', 'election_data.csv')
BALLOT_ID_INDEX = 0
COUNTY_INDEX = 1
CANDIDATE_INDEX = 2

# Set Variables
candidate = []
candidate_votes = []
total_votes = 0


os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(ELECTION_DATA_PATH, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    election_data_dict = {}
    for rows in csvreader:
        election_data_dict = {rows[0]:rows[2] for rows in csvreader}

with open(ELECTION_DATA_PATH) as csvfile:
    csvreader = csv.reader(csvfile)
    # Skip header row
    csv_header = next(csvreader)

    for row in csvreader:
        #candidate.append(row[2])
        #sorted_candidates = sorted(candidate)
        # Inputs
        current_id = row[0]
        current_county = row[1]
        current_candidate = row[2]
        # Calculate total votes
        total_votes += 1
        # List of candidates who received votes
        
        # Percent each candidate won

        # Total votes each candidate won

        # Calculate who received most votes
    
    output_text = (
        " \n"
        "Election Results\n"
        "-----------------------------------------\n"
        "Total Votes: " + str(total_votes) + "\n"
        "-----------------------------------------\n"
        "  :   \n"
        "  :   \n"
        "  :   \n"
        "-----------------------------------------\n"  
        "Winner:   \n"
        "-----------------------------------------\n"
    )

    with open('TEMPOUT', 'w') as out_file:
        out_file.write(output_text) 

print(output_text)




