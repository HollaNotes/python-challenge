import os
import csv

# Set constants
BUDGET_DATA_PATH = os.path.join('Resources', 'budget_data.csv')

# Set Variables
bankdata_dict = {}
months = []
profit_changes = []
current_profit = 0
total_months = 0
total_profit = 0
prev_profit = None
total_change = 0

# Change directory to current python directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))
# Open and read CSV
with open(BUDGET_DATA_PATH) as csvfile:
    csvreader = csv.reader(csvfile)
    # Skip header row 
    csv_header = next(csvreader)
    # Read through each row (except for header)
    for row in csvreader:
        # Inputs
        bankdata_dict[row[0]] = row[1]
        current_date = row[0]
        current_profit = int(row[1])
        # Calculate total months     
        total_months += 1
        # Calculate total profit
        total_profit += current_profit
        # Changes         
        if prev_profit is not None:         
            current_change = current_profit - prev_profit  
            # Sum of changes
            total_change += current_change 
            # Add profit changes to a list
            profit_changes.append(current_change)
            # Add list of the months to a list
            months.append(row[0])
        # Prepare for next row
        prev_profit = current_profit
        # Calculate largest increase       
        greatest_change_increase = max(profit_changes, default=0)       
        # Calculate largest decrease
        greatest_change_decrease = min(profit_changes, default=0)

# Find average change between months        
average_change = round(total_change/(total_months-1) ,2)

# Text to print
output_text = ( 
    f" \n"
    f"Financial Analysis\n"
    f"-----------------------------------------\n"
    f"Total Months: {total_months} \n"
    f"Total: ${total_profit}\n"
    f"Average Change: ${average_change}\n" 
    f"Greatest Increase in Profits: {greatest_change_increase} \n"
    f"Greatest Decrease in Profits: " + "($" + str(greatest_change_decrease) + ")\n"
)
# Write .txt file
with open('TEMPOUT', 'w') as out_file:
    out_file.write(output_text) 

print(output_text)  



