import os
import csv

ELECTION_DATA_PATH = os.path.join('Resources', 'election_data.csv')
BALLOT_ID_INDEX = 0
COUNTY_INDEX = 1
CANDIDATE_INDEX = 2

# Set Variables
total_votes = 0

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(ELECTION_DATA_PATH) as csvfile:
    # CSV reader specifies delimiter   
    csvreader = csv.reader(csvfile)
    # Skip header row
    csv_header = next(csvreader)

    for row in csvreader:
        # Inputs

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
