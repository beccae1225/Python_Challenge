import os
import csv

budget_data_csv = os.path.join('C:/Desktop/git/Python_Challenge/PyBank/Resources/budget_data.csv')

#Define the function 
#def financial_analysis(budget_data):

    #months = int(budget_data[0])
    #profit = int(budget_data[1])
      
    #Total number of months
    #total_months = len(months)
    


with open(budget_data_csv) as csvfile: 
    csvreader = csv.reader(csvfile, delimter=',')
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

for row in csvreader: 

    print(row)
    print(total_months)