import os
import csv


# set path to .csv file
csvpath = os.path.join('PyBank','Resources', 'budget_data.csv')

# create and declare variables for months and total profits 
months = 0
profits = 0

# create variables for greatest profit/loss
greatestp = 0
greatestl = 0
greatsp_month = ""
greatestl_month = ""

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # eliminate the header row
    csv_header = next(csvreader)
    print(f"Bank: {csv_header}")
    
    # use for loop to add all months and profits
    for row in csvreader:
        months += 1
        profits += int(row[1])
    # if current row is greater OR less than current variables then set to current row
        if int(row[1]) > greatestp:
            greatestp = int(row[1])
            greatestp_month = row[0]
        if int(row[1]) < greatestl:
            greatestl = int(row[1])
            greatestl_month = row[0]

# create and calculate variable for avg profits/losses
avg_pl = profits / months
# round average
avg_pl = round(avg_pl, 2)

#print all collected variables
print('Financial Analysis')
print('---------------------')
print(f'Total Months: {months}')
print(f'Total Profits: ${profits}')
print(f'Average Profits: ${avg_pl}')
print(f'Greatest Increase in Profits: {greatestp_month} (${greatestp})')
print(f'Greatest Decrease in Profits: {greatestl_month} (${greatestl})')



