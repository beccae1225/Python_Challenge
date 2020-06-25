import os
import csv 

election_data_csv = os.path.join('Resources', 'election_data.csv')

candidate_list = {row[2]}
candidate = 0
total_votes = 0

with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    #print(f'CSV Header: {csv_header}')

    for row in csvreader:
        #Total Vote Counts
        total_votes = total_votes + 1
        
        #Complete List of Candidates
        for x in candidate_list:
            print(candidate_list)

        #Percentage of Votes per Candidate

        #Total number of votes per candidate 

        #Winner

    #Print statements
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {str(total_votes)}")
    print("-------------------------")
    print(candidate_list)