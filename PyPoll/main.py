import os
import csv
from collections import Counter

ELECTION_DATA_PATH = os.path.join('Resources', 'election_data.csv')
BALLOT_ID_INDEX = 0
COUNTY_INDEX = 1
CANDIDATE_INDEX = 2

# Set Variables
candidate_options = []
candidate_votes = {}
total_votes = 0
winning_candidate = ""
winning_count = 0

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(ELECTION_DATA_PATH) as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:


        # Inputs

        # Calculate total votes
        total_votes += 1
        # List of candidates who received votes
        candidate_name = row["Candidate"]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        # Percent each candidate won
        candidate_votes[candidate_name] += 1
        # Total votes each candidate won
        for candidate in candidate_votes:
            votes = candidate_votes.get(candidate)
            vote_percentage = float(votes) / float(total_votes) * 100
        # Calculate who received most votes
            if (votes > winning_count):
                winning_count = votes
                winning_candidate = candidate


    output_text = (
        f" \n"
        f"Election Results\n"
        f"-----------------------------------------\n"
        f"Total Votes: {total_votes} \n"
        f"-----------------------------------------\n"
        f"  :   \n" 
        f"  :   \n"
        f"  :   \n"
        f"-----------------------------------------\n"  
        f"Winner:   \n"
        f"-----------------------------------------\n"
    )

    with open('TEMPOUT', 'w') as out_file:
        out_file.write(output_text) 

print(output_text)
print(candidate_options)



