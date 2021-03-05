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

    #for loop to count votes
    for row in csvreader:
        total_votes += 1
        #see who has the given vote
        if str(row[2]) == "Khan":
            khan_v += 1
        if str(row[2]) == "Correy":
            correy_v += 1
        if str(row[2]) == "Li":
            li_v += 1
        if str(row[2]) == "O'Tooley":
            otooley_v += 1

#calculate percentage of votes candidates received, round
khan_p = khan_v / total_votes * 100
khan_p = round(khan_p, 3)
correy_p = correy_v / total_votes * 100
correy_p = round(correy_p, 3)
li_p = li_v / total_votes * 100
li_p = round(li_p, 3)
otooley_p = otooley_v / total_votes * 100
otooley_p = round(otooley_p, 3)

# print final totals
print("Election Results")
print("------------------------")
print(f'Total Votes: {total_votes}')
print("------------------------")
print(f'Khan: {khan_p}% ({khan_v})')
print(f'Correy: {correy_p}% ({correy_v})')
print(f'Li: {li_p}% ({li_v})')
print(f"O'Tooley: {otooley_p}% ({otooley_v})")
print("------------------------")
# check which candidate had the most votes
if khan_v > correy_v and khan_v > li_v and khan_v > otooley_v:
    print("Winner: Khan")
elif correy_v > li_v and correy_v > otooley_v:
    print("Winner: Cooley")
elif li_v > otooley_v:
    print("Winner: Li")
else:
    print("Winner: O'Tooley")
print("------------------------")    

