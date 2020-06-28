import os
import csv

budget_data_csv = os.path.join('Resources', 'budget_data.csv')

total_months = 0
total_amount = 0
average_change = 0
prev_rev = 0
revenue_change = 0
changes = []
month_change = []
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
        changes = changes + [revenue_change]
        month_change = month_change + [row[0]]
        
                #Greatest Increase/Decrease in Profit
        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row[0]

        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row[0]

average_change = sum(changes) / len(month_change)

#Print statements

Text = (
    f"Financial Analysis\n" 
    f"---------------------\n" 
    f"Total Months: {total_months}\n" 
    f"Total: ${total_amount}\n"
    f"Average Change: ${average_change}\n" 
    f"Greatest Increase in Profits: {greatest_increase}\n" 
    f"Greatest Decrease in ProfitsL {greatest_decrease}\n" 
) 

print(Text)

output_file = os.path.join("Analysis", "Financial_Analysis.txt")

with open(output_file, "w") as datafile:
   writer = csv.writer(datafile)

   datafile.write(Text)
    
