# Dependencies
import os
import csv

# Set constants
ELECTION_DATA_PATH = os.path.join('Resources', 'election_data.csv')
######## REMOVE???
#BALLOT_ID_INDEX = 0
#COUNTY_INDEX = 1
#CANDIDATE_INDEX = 2

# Set Variables
candidate_options = []
candidate_votes = {}
total_votes = 0
winning_candidate = ""
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
            if (votes > winning_count):
                winning_count = votes
                winning_candidate = candidate

                
    candidate1_votes = candidate_votes.get(candidate_options[0])
    candidate2_votes = candidate_votes.get(candidate_options[1])
    candidate3_votes = candidate_votes.get(candidate_options[2])
    candidate1_percentage = round((candidate1_votes/total_votes),5)
    candidate2_percentage = round((candidate2_votes/total_votes),5)
    candidate3_percentage = round((candidate3_votes/total_votes),5)

    output_text = (
        f" \n"
        f"Election Results\n"
        f"-----------------------------------------\n"
        f"Total Votes: {total_votes} \n"
        f"-----------------------------------------\n"
        f"{candidate_options[0]}  : {(candidate1_percentage)*100}% ({candidate1_votes})  \n" 
        f"{candidate_options[1]}  : {(candidate2_percentage)*100}% ({candidate2_votes})  \n" 
        f"{candidate_options[2]}  : {(candidate3_percentage)*100}% ({candidate3_votes})  \n" 
        f"-----------------------------------------\n"  
        f"Winner: {winning_candidate}  \n"
        f"-----------------------------------------\n"
    )

    with open('TEMPOUT', 'w') as out_file:
        out_file.write(output_text) 

print(output_text)

#####################################
# print(candidate_votes)

# print(list(candidate_votes.keys()))
# print(list(candidate_votes.values()))

# print([key for key in candidate_votes.keys()][1])
# print([value for value in candidate_votes.values()][1])
# print(candidate_name)
# print(candidate_options)
# print(votes)




