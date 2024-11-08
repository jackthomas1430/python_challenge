# PyBank-Financial Analysis

##Description 

The purpose of this project is to examine the financial records of a company. The Python script, "pybank_main.py" analyzes the dataset, "budget_data.csv", and calculates the following values:
    
    -Total number of months included
    -The net total amount of "Profit/Losses"
    -The changes in "Profit/Losses" + the average change over the period 
    -The date and amount of the greatest increase in profits
    -The date and amount of the greatest decrease in profits

The results are printed to the terminal and exported onto the txt file, "financial_analysis.txt", which is located in the "analysis" folder. 

##File Structure
    
    -"python_challenge"(https://github.com/jackthomas1430/python_challenge.git): The main repo for both the PyBank and PyPoll challenges. The PyBank challenge folder contains the main Python script for the election results analysis, a "Resources" folder containing the dataset, and an "anaylsis" folder with the txt file containing the results. 
    -"budget_data.csv": The dataset is located in the "Resources" folder. It contains two columns: "Date" and         
      "Profit/Losses"
    -"pybank_main.py": The main Python script for the PyBank Challenge. Find in the "PyBank" folder inside the     
      "python_challenge" repo
    -"financial_analysis.txt": The txt file with the results of the anyalsis. Located in the "analysis" folder inside the "PyBank" Folder 
    
##Instructions
   
    1. Clone the repository to your local device using git clone https://github.com/jackthomas1430/python_challenge.git
    2. Check that the "budget_data.csv" is located in the "Resources" folder
    3. Run the script: python pybank_main.py 

##Results
    
    The following results will display to the terminal and be saved to the "financial_analyisis.txt" file.
    
Financial Analysis

----------------------------

Total Months: 86

Total: $22564198

Average Change: $-8311.11

Greatest Increase in Profits: Aug-16 ($1862002)

Greatest Decrease in Profits: Feb-14 ($-1825558)

##Screenshots

![PyBank Results Printed to Terminal](python_challenge/PyBank/Resources/pybank_terminal_results.png)

##Acknowledgements
    
    Xpert Learning Assistant was used to establish the framework and logic for this code, answer detailed questions, and assist in debugging. The framework and code were modified using course curriculum and activities to fit the requirements of the assignment.For more information about the Xpert Learning Assistant, visit [EdX Xpert Learning Assistant](https://www.edx.org/). 

##References

Data for this dataset was generated by edX Boot Camps LLC

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
