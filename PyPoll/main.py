# This will allow us to create file path across OS
import os

# Module for reading CSV files
import csv

# Specify the file we will be using
election_data_csv = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')
print(f'election_data_csv: {election_data_csv}')



# Set Variables
total_votes = 0



with open(election_data_csv) as csvfile:
#   CSV reader specifies delimiter   
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

#   Read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

#------PRINT CSV ROWS---------------------------------------------------
#   Read each row of data after the header      
    #for row in csvreader:
        #print(row)
#-----------------------------------------------------------------------
#      
# 1 ------TOTAL VOTES CAST----------------------------------------------
    # Count begins at zero and needs to increase by 1 as it counts the rows   
   
    for row in csvreader:
        total_votes += 1
    
# 1 --------------------------------------------------------------------
#
# 2 ------COMPLETE LIST OF CANDIDATES WHO RECEIVED VOTES----------------


# 2 --------------------------------------------------------------------
#
# 3 ------PERCENTAGE OF VOTES EACH CANDIDATE WON------------------------



# 3 --------------------------------------------------------------------
#
# 4 ------TOTAL NUMBER OF VOTES EACH CANDIDATE WON----------------------



# 4 --------------------------------------------------------------------
#
# 5 ------THE WINNER OF THE ELECTION BASED ON POPULAR VOTE--------------



# 5 --------------------------------------------------------------------

# 6 ------PRINT ALL------------------------------------------------------------------
   
    print(" ")
    print(f"Election Results")
    print(f"-----------------------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"-----------------------------------------")
    print(f"  :   ")
    print(f"  :   ")
    print(f"  :   ")   
    print(f"-----------------------------------------")     
    print(f"Winner:   ")
    print(f"-----------------------------------------")  


# 6 ---------------------------------------------------------------------------------