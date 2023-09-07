# This will allow us to create file path across OS
import os

# Module for reading CSV files
import csv

# Specify the file we will be using
csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')
print(f'csvpath: {csvpath}')

with open(csvpath) as csvfile:
#   CSV reader specifies delimiter   
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

#   Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#-----------------------------------------------------------------------
#   Read each row of data after the header      
    #for row in csvreader:
        #print(row)
#-----------------------------------------------------------------------        
      