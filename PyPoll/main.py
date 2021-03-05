import os
import csv

# Set path for file
csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

#create and set variables for total votes and votes per candidate
total_votes = 0
khan_v = 0
correy_v = 0
li_v = 0
otooley_v = 0
# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # eliminate the header row
    csv_header = next(csvreader)
    print(f"Polls: {csv_header}")

    #for loop to count votes
    for row in csvreader:
        total_votes += 1
        #see who has the given vote
        
    

