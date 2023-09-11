# This will allow us to create file path across OS
import os

# Module for reading CSV files
import csv

# Specify the file we will be using
budget_data_csv = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')
print(f'budget_data_csv: {budget_data_csv}')

# Define funtions
 


# Set Variables
#budget_data_dict = {}
dates = []
profit_loss = []
total_months = 0
pl_total_net = 0



with open(budget_data_csv, 'r') as csvfile:
#   CSV reader specifies delimiter     
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    #budget_data_dict = {rows[0]:rows[1] for rows in csvreader}
    
    #   Read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    

#------PRINT CSV ROWS----------------------------------------------------------------
#   Read each row of data after the header    
    #for row in csvreader:
        #print(row)    
#------------------------------------------------------------------------------------ 
#        
# 1 ------TOTAL MONTHS IN DATASET----------------------------------------------------
    # Count begins at zero and needs to increase by 1 as it counts the rows
      
    for row in csvreader:
        total_months += 1

        
    
# 1 ---------------------------------------------------------------------------------  
#   
# 2 ------NET TOTAL AMOUNT OF PROFIT/LOSS OVER ENTIRE PERIOD-------------------------
    # Need to get sum of entire column as it goes through the rows   
   
        
        

    

# 2 ---------------------------------------------------------------------------------

# 3 ------CHANGES IN PROFIT/LOSS OVER ENTIRE PERIOD, AND AVERAGE OF CHANGES----------


# 3 ---------------------------------------------------------------------------------

# 4 ------GREATEST INCREASE IN PROFITS (DATE AND AMOUNT) OVER ENTIRE PERIOD----------


# 4 ---------------------------------------------------------------------------------

# 5 ------GREATEST DECREASE IN PROFITS (DATE AND AMOUNT) OVER ENTIRE PERIOD----------


# 5 ---------------------------------------------------------------------------------

# 6 ------PRINT ALL------------------------------------------------------------------
print(" ")
print(f"Financial Analysis")
print(f"-----------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: $  ")
print(f"Average Change: $  ")
print(f"Greatest Increase in Profits:   ")
print(f"Greatest Decrease in Profits:   ")

# 6 ---------------------------------------------------------------------------------
