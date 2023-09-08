# This will allow us to create file path across OS
import os

# Module for reading CSV files
import csv

# Specify the file we will be using
budget_data_csv = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')
print(f'budget_data_csv: {budget_data_csv}')

with open(budget_data_csv) as csvfile:
#   CSV reader specifies delimiter     
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

#   Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    

#------PRINT CSV ROWS---------------------------------------------------
#   Read each row of data after the header    
    #for row in csvreader:
        #print(row)    
#-----------------------------------------------------------------------        

#------TOTAL MONTHS-----------------------------------------------------
    # Count begins at zero and needs to increase by 1 as it counts the rows
    count = 0
    for row in csvreader:
        count += 1
    print(f'Total Months: {count}')  
#------------------------------------------------------------------------    

#------TOTAL-------------------------------------------------------------


