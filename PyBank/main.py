import os
import csv


# Set path for file
csvpath = os.path.join("..", "Resources", "budget_data.csv")


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



