import os
import csv

# Set path for file
csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')


# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # eliminate the header row
    csv_header = next(csvreader)
    print(f"Polls: {csv_header}")

    

