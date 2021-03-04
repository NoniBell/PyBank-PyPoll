import os
import csv


# set path to .csv file
csvpath = os.path.join('PyBank','Resources', 'budget_data.csv')

# create and declare variables for months and total profits 
months = 0
profit_loss = 0

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # eliminate the header row
    csv_header = next(csvreader)
    print(f"Bank: {csv_header}")
    
    for row in csvreader:
         months += row[0]
        profit_loss += row[1]

#create and calculate variable for avg profits/losses
avg_pl = profit_loss / len(csvreader)

print(f'Total Profits: ${profit_loss}')
print(f'Total Months: {months}')
print(f'Average Profits: ${avg_pl}')



