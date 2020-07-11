import os
import csv

election_data_csv = os.path.join("Resources", "election_data.csv")

total_votes = 0

candidate_list = []
vote_counts = []
unique_list = []
vote_percents = []

with open(election_data_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    print(csv_header)

    for i in csvreader:

        #Vote Count
        total_votes = total_votes + 1

        #Candidate Names to List
        candidate_list.append(i[2])

        for j in candidate_list:
            unique_list.append(j)

            #Total Votes per Candidate
            votes = candidate_list.count(j)
            vote_counts.append(votes)

            #Percentage of Votes
            percent = (votes/total_votes) * 100
            vote_percents.append(percent)

        most_votes = max(vote_counts)
        winner = unique_list[vote_counts.index(most_votes)]


print("Election Results\n") 
print("---------------------------\n")  
print(f"Total Votes: {total_votes}\n") 
for i in range(len(unique_list)):
    print(unique_list[i] + ":" + str(vote_percents[i]) + "% (" + str(vote_counts[i])+ ")")
v

output_file = os.path.join("Analysis", "Vote_results.txt")
with open(output_file, "w") as datafile: 
    writer = csv.writer(datafile)

    datafile.write(f"Election Results\n")
    datafile.write(f"----------------------\n")
    datafile.write(f"Total Votes: {total_votes}\n")

    for i in range(len(unique_list)):
        datafile.write(f"{unique_list[i]}: {str(vote_percents[i])}% ({str(vote_counts[i])})\n")

    datafile.write(f"--------------------")
    datafile.write(f"The winner is: {winner}")


