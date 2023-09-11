# Dependencies
import os
import csv

# Set constants
ELECTION_DATA_PATH = os.path.join('Resources', 'election_data.csv')

# Set Variables
candidate_options = []
candidate_votes = {}
total_votes = 0
winning_count = 0

# Change directory to current python directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))
# Open and read CVS
with open(ELECTION_DATA_PATH) as csvfile:
    # Create dict
    csvreader = csv.DictReader(csvfile)
    # Read through each row
    for row in csvreader:
        # Inputs
        # Calculate total votes
        total_votes += 1
        # List of candidates who received votes
        candidate_name = row["Candidate"]
        # Separate unique candidates
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        # Add votes to each candidate at it loops though
        candidate_votes[candidate_name] += 1
        # Read through vote counts to find winner
        for candidate in candidate_votes:
            # Get vote count and percentage
            votes = candidate_votes.get(candidate)
            vote_percentage = (votes / (total_votes)) * 100

        # Determine who received most votes
        winning_candidate = max(zip(candidate_votes.values(), candidate_votes.keys()))[1]    

    # Check to see how many candidates and values for next portion, then comment them out
        # print(list(candidate_votes.keys()))
        # print(list(candidate_votes.values()))
        
    # Determined there are 3 candidates, so getting votes and percentage for each                 
    candidate1_votes = candidate_votes.get(candidate_options[0])
    candidate2_votes = candidate_votes.get(candidate_options[1])
    candidate3_votes = candidate_votes.get(candidate_options[2])
    candidate1_percentage = round((candidate1_votes/total_votes),5)
    candidate2_percentage = round((candidate2_votes/total_votes),5)
    candidate3_percentage = round((candidate3_votes/total_votes),5)
    
    # Text to print
    output_text = (
        f" \n"
        f"Election Results\n"
        f"-----------------------------------------\n"
        f"Total Votes: {total_votes} \n"
        f"-----------------------------------------\n"
        f"{candidate_options[0]}  : {round((candidate1_percentage * 100),5)}% ({candidate1_votes})  \n" 
        f"{candidate_options[1]}  : {round((candidate2_percentage * 100),5)}% ({candidate2_votes})  \n" 
        f"{candidate_options[2]}  : {round((candidate3_percentage * 100),5)}% ({candidate3_votes})  \n" 
        f"-----------------------------------------\n"  
        f"Winner: {winning_candidate}  \n"
        f"-----------------------------------------\n"
    )
    # Write .txt file
    with open('TEMPOUT', 'w') as out_file:
        out_file.write(output_text) 

print(output_text)






