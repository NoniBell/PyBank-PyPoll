import os
import csv


# set path to .csv file
csvpath = os.path.join("PyBank","Resources", "budget_data.csv")


# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#declare months and profits/losses variables
months = 0
profit_loss = 0

#use for loop to calculate the total months and net total profits/losses
for row in csvreader:
    months += row[0]
    profit_loss += row[1]

#create and calculate variable for avg profits/losses
avg_pl = profit_loss / len(csvreader)

print(f'Total Profits: ${profit_loss}')
print(f'Total Months: {months}')
print(f'Average Profits: ${avg_pl}')