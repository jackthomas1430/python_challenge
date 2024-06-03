import os
import csv

# Path to collect data 
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Initialize total months + profit losses variables
total_months = 0
total = 0
#Track previous profit/loss. Set = None so that it starts at the first point of change within the dataset.
previous_change = None
#Initialize lists to track monthly change in profits/losses and the corresponding date
changes = []
months = []
#Initialize dictionaries to track greatest increase and decrease
#Convert amount value to float 
greatest_increase = {'date': None, 'amount': float()}
greatest_decrease = {'date': None, 'amount': float()}

# Open the CSV file and store header row 
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
 ##Loop through each row in csv; dates in first column, profits in the second column 
    for row in csvreader:
        date = row[0]
        profit = int(row[1])
##Calculate total months and total net profit
        total_months += 1
        total += int(profit)
        
        #Check that the previous change has a value to ensure that the loop starts at the first change value and ends at the last
        # Calculate monthly changes; add change to changes list and corresponding dates to months list
        if previous_change is not None:
            change = profit - previous_change
            changes.append(change)
            months.append(date)
            
            # Calculate greatest increase
            #If the current change is greater than the current greatest increase, the greatest_increase list now = the current amount and date
            if change > greatest_increase['amount']:
                greatest_increase['amount'] = change
                greatest_increase['date'] = date
            
            # Calculate greatest decrease
            if change < greatest_decrease['amount']:
                greatest_decrease['amount'] = change
                greatest_decrease['date'] = date
        
        # Update previous_change to continue loop
        previous_change = profit

# Calculate the average change
average_change = sum(changes) / len(changes)

#The results
results = (
    "\n"
    "Financial Analysis\n\n"
    "----------------------------\n\n"
    f"Total Months: {total_months}\n\n"
    f"Total: ${total}\n\n"
    f"Average Change: ${average_change:.2f}\n\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)

# Print the results to the terminal
print(results)

#Export the results to a text file
with open('financial_analysis.txt', 'w') as file:
    file.write(results)
