import os
import csv

election_data_csv = os.path.join("Resources", "election_data.csv")

total_votes = 0
votes_per_person = 0
candidate_list = []
vote_counts = []
unique_list = []
vote_percents = []
max_vote_count = 0


with open(election_data_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    #print(csv_header)

    for i in csvreader:

        #Vote Count
        total_votes = total_votes + 1

        #Candidate Names to List
        candidate_list.append(i[2])

        #check list for candidate
        if i[2] not in unique_list:
            unique_list.append(i[2])


print("Election Results\n")
print("---------------------------\n")  
print(f"Total Votes: {total_votes}\n")
print("---------------------------\n")  
for i in unique_list:
    votes_per_person = 0
    for v in candidate_list:
        if i == v:
            votes_per_person = votes_per_person + 1

    if max_vote_count < votes_per_person:
        max_vote_count = votes_per_person
        winner = i
    percent = round(((votes_per_person/total_votes) * 100),5)
    print(i + ": " + str(percent) + "% (" + str( votes_per_person) + ")" +"\n")
print("-----------------------------\n")
print(f"The winner is: {winner}")
print("-----------------------------\n")

output_file = os.path.join("Analysis", "Vote_results.txt")
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    datafile.write(f"Election Results\n")
    datafile.write(f"----------------------\n")
    datafile.write(f"Total Votes: {total_votes}\n")

    for i in range(len(unique_list)):
        datafile.write(f"{i} :  {str(percent)} % ( {str(votes_per_person)})\n")

    datafile.write(f"--------------------")
    datafile.write(f"The winner is: {winner}")