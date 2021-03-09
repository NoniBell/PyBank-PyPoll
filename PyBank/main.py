import os
import csv


# set path to .csv file
csvpath = os.path.join('PyBank','Resources', 'budget_data.csv')

# create and declare variables for months, monthly profit, and total profits 
months = 0
profits = 0
m_profit = 0
#create an empty list for profit changes
profit_change = []

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
    
    # use for loop to add all months and profits
    for row in csvreader:
        months += 1
        profits += int(row[1])
        #collect monthly profit and append to profit_change list
        m_profit = int(row[1])
        profit_change.append(m_profit) 
    # if current row is greater OR less than current variables then set to current row
        if int(row[1]) > greatestp:
            greatestp = int(row[1])
            greatestp_month = row[0]
        if int(row[1]) < greatestl:
            greatestl = int(row[1])
            greatestl_month = row[0]

# create and calculate variable for avg change
avg_pl = sum(profit_change) / len(profit_change)


#print all collected variables
print('Financial Analysis')
print('---------------------')
print(f'Total Months: {months}')
print(f'Total Profits: ${profits}')
print(f'Average Change: ${avg_pl}')
print(f'Greatest Increase in Profits: {greatestp_month} (${greatestp})')
print(f'Greatest Decrease in Profits: {greatestl_month} (${greatestl})')

#print all variables to .txt file
with open("bank.txt", "a") as b:
    print('Financial Analysis', file=b)
    print('---------------------', file=b)
    print(f'Total Months: {months}', file=b)
    print(f'Total Profits: ${profits}', file=b)
    print(f'Average Change: ${avg_pl}', file=b)
    print(f'Greatest Increase in Profits: {greatestp_month} (${greatestp})', file=b)
    print(f'Greatest Decrease in Profits: {greatestl_month} (${greatestl})', file=b)

