import os
import csv

# Path to collect data 
election_csv = os.path.join('Resources', 'election_data.csv')

# Initialize variables for total number of votes, winner, and most votes
# Create dictionary to store election results by candidate
total_votes = 0
election_results = {}
winner = ""
most_votes = 0

#Open CSV file and store header 
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)

 # Loop through data in csv to calculate votes; add up total votes; candidate name stored in column 3 
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        #Check if candidate is already in election results dictionary. Add to vote count or sets vote count to 1 
        if candidate in election_results:
            election_results[candidate] += 1
        else:
            election_results[candidate] = 1

    # Create string to print total votes result
results = (
        "\n"
        f"Election Results\n\n"
        f"-------------------------\n\n"
        f"Total Votes: {total_votes}\n\n"
        f"-------------------------\n\n")
    
#Calculate the winner
#Loop through every candidate + vote count in election_results dictionary 
#Calculate percentage of votes each cadidate received
#Add candidate name, % votes, and total votes to results
for candidate, votes in election_results.items():
    percentage = (votes / total_votes) * 100
    results += f"{candidate}: {percentage:.3f}% ({votes})\n\n"
    #Calculate most votes
    #Check if candidate has more votes than the max recorded
    #Update winner and most votes
    if votes > most_votes:
            winner = candidate
            most_votes = votes
# Add the winner to results
results += (
    f"-------------------------\n\n"
    f"Winner: {winner}\n\n"
    f"-------------------------\n\n"
)

# Print results to terminal
print(results)

# Export to text file
with open("election_results.txt", "w") as file:
    file.write(results)
