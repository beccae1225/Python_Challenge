import os
import csv

budget_data_csv = os.path.join('Resources', 'budget_data.csv')

total_months = 0
total_amount = 0
average_change = 0
prev_rev = 0
revenue_change = 0
changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

with open(budget_data_csv, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:

        #Total number of months
        total_months = total_months + 1            

        #Net Profit/Loss
        total_amount = total_amount + int(row[1]) 
              
        #Average of the changes in Profit/Loss
        revenue_change = int(row[1]) - prev_rev
        prev_rev = int(row[1])
        
                #Greatest Increase/Decrease in Profit
        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row[0]

        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row[0]

    changes.append(revenue_change)
    change = list(changes)
    average_change = sum(change)/len(change)

    #Print statements
    print("Financial Analysis")
    print("--------------------------------------")
    print(f"Total Months: {str(total_months)}")
    print(f"Total: ${str(total_amount)}")
    print(f"Average Change: ${str(average_change)}")
    print(f"Greatest Increase in Profits: {str(greatest_increase)}")
    print(f"Greatest Decrease in Profits: {str(greatest_decrease)}")
    

output_file = os.path.join("Analysis", "Financial_Analysis.txt")

with open(output_file, "w") as datafile:
   writer = csv.writer(datafile)
    
