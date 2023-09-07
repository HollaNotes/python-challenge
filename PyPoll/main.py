import os
import csv


csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')
print(f'csvpath: {csvpath}')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    for row in csvreader:
        print(row)
      