import os
import csv


BUDGET_DATA_PATH = os.path.join('Resources', 'budget_data.csv')
DATE_INDEX = 0
PROFIT_INDEX = 1

# Set Variables
total_months = 0
total_profit = 0
prev_profit = None
total_change = 0

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(BUDGET_DATA_PATH) as csvfile:
    csvreader = csv.reader(csvfile)
    # Skip header row 
    csv_header = next(csvreader)
      
    for row in csvreader:
        # Inputs
        current_date = row[0]
        current_profit = int(row[1])
        # Calculate total months     
        total_months += 1
        # Calculate total profit
        total_profit += current_profit
        # Changes         
        if prev_profit is not None:         
            current_change = current_profit - prev_profit  
            total_change += current_change 
        prev_profit = current_profit     # prepare for next row
        # Calculate largest increase
        
        # Calculate largest decrease 

average_change = round(total_change/(total_months-1) ,2)

output_text = ( 
    " \n"
    "Financial Analysis\n"
    "-----------------------------------------\n"
    "Total Months: " + str(total_months) + "\n"
    "Total: $" + str(total_profit) + "\n"
    "Average Change: $" + str(average_change) + "\n" 
    "Greatest Increase in Profits:   \n"
    "Greatest Decrease in Profits:   \n"
)

with open('TEMPOUT', 'w') as out_file:
    out_file.write(output_text) 

print(output_text)    